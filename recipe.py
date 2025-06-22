from datetime import datetime
from . import db

class Recipe(db.Model):
    __tablename__ = 'recipes'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    cooking_time = db.Column(db.Integer)  # в минутах
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))