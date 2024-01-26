from flask import Blueprint, request, jsonify

from infrastructure.DogRepository import DogRepository
from domain.Dog import Dog

dog_api = Blueprint('dogs', __name__)

@dog_api.route('/dogs', methods=['GET'])
def get_dogs():
    dog_repo = DogRepository()
    filters = {
        "gender": request.args.get('gender'),
        "special_needs": request.args.getlist('special_needs'),
        "min_size": request.args.get('min_size'),
        "max_size": request.args.get('max_size')
    }

    sort_criteria = {
        "birth_year": request.args.get('birth_year')
    }

    return jsonify([dog.to_json() for dog in dog_repo.get(filters, sort_criteria)])

@dog_api.route('/dogs', methods=['POST'])
def add_dog():
    dog_repo = DogRepository()
    new_dog = Dog.from_json(request.get_json())
    return jsonify(dog_repo.add(new_dog).to_json())

@dog_api.route('/dogs/<id>', methods=['GET'])
def get_dog_by_id(id):
    dog_repo = DogRepository()
    return jsonify(dog_repo.get_by_id(str(id)).to_json())

@dog_api.route('/dogs/<id>', methods=['PUT'])
def update_dog(id):
    dog_repo = DogRepository()
    updated_dog = Dog.from_json(request.get_json())
    return jsonify(dog_repo.update(str(id), updated_dog).to_json())

@dog_api.route('/dogs/<id>', methods=['DELETE'])
def delete_dog(id):
    dog_repo = DogRepository()
    return jsonify(dog_repo.remove(str(id)).to_json())