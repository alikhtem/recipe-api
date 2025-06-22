from flask_restful import Resource, reqparse
from models.recipe import Recipe
from schemas.recipe_schema import recipe_schema, recipes_schema

class RecipeResource(Resource):
    def get(self, recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        return recipe_schema.dump(recipe)
    
    def put(self, recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        parser = self._get_parser()
        args = parser.parse_args()
        
        recipe.title = args['title']
        recipe.ingredients = args['ingredients']
        recipe.instructions = args['instructions']
        recipe.cooking_time = args['cooking_time']
        recipe.category_id = args['category_id']
        
        db.session.commit()
        return recipe_schema.dump(recipe)
    
    def _get_parser(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('ingredients', required=True)
        parser.add_argument('instructions', required=True)
        parser.add_argument('cooking_time', type=int)
        parser.add_argument('category_id', type=int)
        return parser