from flask import Blueprint, request, jsonify
from infrastructure.DogRepository import DogRepository
from domain.Dog import Dog

dog_api = Blueprint('dogs', __name__)

@dog_api.route('/dogs', methods=['GET'])
def get_dogs():
    dog_repo = DogRepository()
    return jsonify([dog.to_json() for dog in dog_repo.get()])

@dog_api.route('/dogs', methods=['POST'])
def add_dog():
    dog_repo = DogRepository()
    new_dog = Dog.from_json(request.get_json())
    return jsonify(dog_repo.add(new_dog).to_json())

@dog_api.route('/dogs/<id>', methods=['GET'])
def get_dog_by_id(id):
    dog_repo = DogRepository()
    return jsonify(dog_repo.get_by_id(int(id)).to_json())

@dog_api.route('/dogs/<id>', methods=['PUT'])
def update_dog(id):
    dog_repo = DogRepository()
    updated_dog = Dog.from_json(request.get_json())
    return jsonify(dog_repo.update(int(id), updated_dog).to_json())

@dog_api.route('/dogs/<id>', methods=['DELETE'])
def delete_dog(id):
    dog_repo = DogRepository()
    return jsonify(dog_repo.remove(int(id)).to_json())