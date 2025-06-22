from marshmallow import Schema, fields, validate

class RecipeSchema(Schema):
    class Meta:
        fields = ('id', 'title', 'ingredients', 'instructions', 
                 'cooking_time', 'created_at', 'category_id')
        
    title = fields.Str(required=True, validate=validate.Length(min=3))
    cooking_time = fields.Int(validate=validate.Range(min=1))
        
recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)