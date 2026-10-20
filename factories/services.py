from fastapi import Depends
from sqlalchemy.orm import Session

from db import get_db
from services.categories_services import CategoryService


def create_category_service(_repository: Session = Depends(get_db)) -> CategoryService:
    return CategoryService(_repository)