from flask import Blueprint, jsonify
from app.models import Item
from app.schemas import ItemSchema
from app.database import db

bp = Blueprint('item_routes', __name__)
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

@bp.route('/items', methods=['GET'])
def get_items():
    items = db.session.query(Item).all()
    return jsonify(items_schema.dump(items))


@bp.route('/items', methods=['GET'])
