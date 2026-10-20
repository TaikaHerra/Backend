from sqlalchemy.orm import Session

import models
from dtos.categories import CreateCategoryReq
from services.abc_categories_service import ABCCategoryService


class CategoryService(ABCCategoryService):

    def __init__(self, _repository: Session):
        self._repository = _repository

    def create(self, req: CreateCategoryReq) -> models.Category:
        category = models.Category(name=req.name)

        self._repository.add(category)
        self._repository.commit()

        return category