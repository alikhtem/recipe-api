from flask_restful import Resource, reqparse
from models.category import Category
from schemas.category_schema import category_schema, categories_schema

class CategoryListResource(Resource):
    def get(self):
        categories = Category.query.all()
        return categories_schema.dump(categories)
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('description')
        args = parser.parse_args()
        
        new_category = Category(name=args['name'], description=args['description'])
        db.session.add(new_category)
        db.session.commit()
        
        return category_schema.dump(new_category), 201