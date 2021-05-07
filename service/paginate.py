import math
from typing import TypeVar, Generic, Type

from model.response import Page

T = TypeVar('T')


class MongoDBPage(Generic[T]):
    def __init__(self, collection, constructor: Type[T]):
        self._collection = collection
        self._constructor = constructor

    async def paginate(self, page=1, page_size=100, filter_=None, sort=None) -> Page[T]:
        if filter_ is None:
            filter_ = {}

        skip = (page - 1) * page_size
        limit = page_size

        total = await self._collection.count_documents(filter_)
        cursor = self._collection.find(filter=filter_, skip=skip, limit=limit, sort=sort)

        items = [self._constructor(**r) async for r in cursor]

        return Page[T](
            total=total,
            pages=math.ceil(total / page_size),
            page=page,
            page_size=page_size,
            items=items,
            count=len(items)
        )
