from flask import Blueprint, request, jsonify


bp = Blueprint('users', __name__)

@bp.route('/', methods=['GET'])
def get_users():
    return 'hello world!'
