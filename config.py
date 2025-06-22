import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ваш_секретный_ключ'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///recipes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-секрет'