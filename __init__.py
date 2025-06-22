from flask_sqlalchemy import SQLAlchemy

# Инициализация SQLAlchemy
db = SQLAlchemy()

# Импорт моделей после создания db, чтобы избежать circular imports
from .category import Category
from .recipe import Recipe

__all__ = ['db', 'Category', 'Recipe']