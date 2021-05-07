import uvicorn
from fastapi import FastAPI

from api.router import router as api_router
from core.events import create_start_app_handler, create_stop_app_handler


def get_application() -> FastAPI:
    application = FastAPI()

    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.include_router(api_router)

    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
