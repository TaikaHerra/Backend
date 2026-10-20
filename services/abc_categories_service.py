import abc


import models
from dtos.categories import CreateCategoryReq


class ABCCategoryService(abc.ABC):
    @abc.abstractmethod
    def create(self, req: CreateCategoryReq) -> models.Category:
        raise NotImplementedError()