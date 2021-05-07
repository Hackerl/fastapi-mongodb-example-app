from typing import TypeVar, Generic, Optional, List

from bson import ObjectId
from pydantic import BaseModel, validator
from pydantic.generics import GenericModel

T = TypeVar('T')


class Error(BaseModel):
    code: int
    message: str


class Page(GenericModel, Generic[T]):
    total: int
    count: int
    pages: int
    page: int
    page_size: int
    items: List[T]


class Response(GenericModel, Generic[T]):
    data: Optional[T]
    error: Optional[Error]

    @validator('error', always=True)
    def check_consistency(cls, v, values):
        if v is not None and values['data'] is not None:
            raise ValueError('must not provide both data and error')

        if v is None and values.get('data') is None:
            raise ValueError('must provide data or error')

        return v

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
