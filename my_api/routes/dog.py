from flask import Blueprint
from services.dog import create_dog_service
#get_dogs_service, get_dog_service, update_dog_service, delete_dog_service

dog = Blueprint('dog', __name__)

@dog.route('/breed/<raza>', methods=['GET'])
def create_dog(raza):
    print('10')
    return create_dog_service(raza) #se ejecuta ese servicio
"""

@dog.route('/', methods=['GET']) #metodo para obtener todas las solicitudes
def get_dogs():
    return get_dogs_service()

@dog.route('/breed/<raza>', methods=['GET'])
def get_dog(raza):
    return get_dog_service(raza)

"
@dog.route('/', methods=['POST'])
def create_dog():
    return create_dog_service() #se ejecuta ese servicio

@dog.route('/<id>', methods=['PUT'])
def update_dog(id):
    return update_dog_service(id)

@dog.route('/<id>', methods=['DELETE'])
def delete_dog(id):
    return delete_dog_service(id)"
"""