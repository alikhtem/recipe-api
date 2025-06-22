from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import Config
from resources.recipe_resources import RecipeResource, RecipeListResource
from resources.category_resources import CategoryListResource

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
api = Api(app)

# Регистрация ресурсов
api.add_resource(RecipeListResource, '/api/recipes')
api.add_resource(RecipeResource, '/api/recipes/<int:recipe_id>')
api.add_resource(CategoryListResource, '/api/categories')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)