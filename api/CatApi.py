from flask import Blueprint, request, jsonify
from infrastructure.CatRepository import CatRepository
from domain.Animal import Animal

cat_api = Blueprint('cats', __name__)

@cat_api.route('/cats', methods=['GET'])
def getCats():
    cat_repo = CatRepository()
    return jsonify([cat.to_json() for cat in cat_repo.get()])

@cat_api.route('/cats', methods=['POST'])
def addCat():
    cat_repo = CatRepository()
    new_cat = Animal.from_json(request.get_json())
    return jsonify(cat_repo.add(new_cat).to_json())

@cat_api.route('/cats/<id>', methods=['GET'])
def get_cat_by_id(id):
    cat_repo = CatRepository()
    return jsonify(cat_repo.get_by_id(int(id)).to_json())

@cat_api.route('/cats/<id>', methods=['PUT'])
def update_cat(id):
    cat_repo = CatRepository()
    updated_cat = Animal.from_json(request.get_json())
    return jsonify(cat_repo.update(int(id), updated_cat).to_json())

@cat_api.route('/cats/<id>', methods=['DELETE'])
def delete_cat(id):
    cat_repo = CatRepository()
    return jsonify(cat_repo.remove(int(id)).to_json())