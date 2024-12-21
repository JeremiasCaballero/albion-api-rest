from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.database import db
from app.models import Material, Category, Item, ItemMaterial


class MaterialSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Material
        sqla_session = db.session
        include_fk = True

    id = fields.Int(dump_only=True)  # Solo lectura
    name = fields.Str(required=True)
    tier = fields.Int(required=True)
    image_path = fields.Str(required=True)


class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        sqla_session = db.session
        include_fk = True

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class ItemMaterialSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ItemMaterial
        sqla_session = db.session
        include_fk = True

    id = fields.Int(dump_only=True)
    item_id = fields.Int(required=True)
    material_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

    # Relaciones
    material = fields.Nested('MaterialSchema', only=('id', 'name', 'tier'))


class ItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        sqla_session = db.session
        include_fk = True

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    tier = fields.Int(required=True)
    user_artefact = fields.Bool(required=False)
    image_path = fields.Str(required=True)

    # Relaciones
    category = fields.Nested('CategorySchema', only=('id', 'name'), required=True)
    materials = fields.Nested('ItemMaterialSchema', many=True, dump_only=True)
