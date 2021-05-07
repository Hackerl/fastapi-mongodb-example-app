from model import MongoDBModel


class Machine(MongoDBModel):
    cpu: int
    memory: int
