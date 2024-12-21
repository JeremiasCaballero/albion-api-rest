from app.database import db

class Material(db.Model):
    __tablename__ = 'materials'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tier = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.String(255), nullable=False)


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tier = db.Column(db.Integer, nullable=False)
    user_artefact = db.Column(db.Boolean, nullable=True)
    image_path = db.Column(db.String(255), nullable=False)

    # Relación con Category
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='items2')

    # Relación con Materiales y cantidades a través de la tabla intermedia
    materials = db.relationship('ItemMaterial', back_populates='item')


class ItemMaterial(db.Model):
    __tablename__ = 'item_materials'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey('materials.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    # Relaciones
    item = db.relationship('Item', back_populates='materials')
    material = db.relationship('Material', backref='item_materials')


    

    ## Relaciones categoria
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='items')

