from flask import Blueprint
from infrastructure.PersonRepository import PersonRepository

person_api = Blueprint('people', __name__)

@person_api.route('/people', methods=['GET'])
def handleIndex():
    return []