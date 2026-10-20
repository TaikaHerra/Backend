from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

import dtos
import models
from db import get_db
from dtos.categories import CreateCategoryReq, CategoryDto
from factories.services import create_category_service
from services.abc_categories_service import ABCCategoryService



router = APIRouter(prefix="/api/categories", tags=["categories"])

CategoryServ = Annotated[ABCCategoryService, Depends(create_category_service)]



@router.post('/', status_code=status.HTTP_201_CREATED)
def create_category(_service: CategoryServ, req: CreateCategoryReq) -> CategoryDto:
    category = _service.create(req)
    return CategoryDto.model_validate(category)


@router.get('/')
def create_all(_repository: Session = Depends(get_db)):
    # cur.execute("SELECT * FROM categories")
    # categories = cur.fetchall()
    _qry = _repository.query(models.Category)
    categories = _qry.all()
    return categories