from marshmallow import Schema, fields

class CategorySchema(Schema):
    class Meta:
        fields = ('id', 'name', 'description')
        
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)