from flask import Blueprint, request, jsonify
from uuid import uuid4

from infrastructure.CatRepository import CatRepository
from domain.Cat import Cat

cat_api = Blueprint('cats', __name__)

@cat_api.route('/cats', methods=['GET'])
def get_cats():
    cat_repo = CatRepository()
    filters = {
        "gender": request.args.get('gender'),
        "special_needs": request.args.getlist('special_needs')
    }

    sort_criteria = {
        "birth_year": request.args.get('birth_year')
    }

    return jsonify([cat.to_json() for cat in cat_repo.get(filters, sort_criteria)])

@cat_api.route('/cats', methods=['POST'])
def add_cat():
    cat_repo = CatRepository()
    new_cat = Cat.from_json(request.get_json())
    return jsonify(cat_repo.add(new_cat).to_json())

@cat_api.route('/cats/<id>', methods=['GET'])
def get_cat_by_id(id):
    cat_repo = CatRepository()
    return jsonify(cat_repo.get_by_id(str(id)).to_json())

@cat_api.route('/cats/<id>', methods=['PUT'])
def update_cat(id):
    cat_repo = CatRepository()
    updated_cat = Cat.from_json(request.get_json())
    return jsonify(cat_repo.update(str(id), updated_cat).to_json())

@cat_api.route('/cats/<id>', methods=['DELETE'])
def delete_cat(id):
    cat_repo = CatRepository()
    return jsonify(cat_repo.remove(str(id)).to_json())