from flask import request, Response
from bson import json_util, ObjectId
from datetime import date
import requests
from config.mongodb import mongo

def create_dog_service(raza): 
    url_api = 'https://dog.ceo/api/breed/'
    url_api += raza
    url_api += '/images/random'
    
    r = requests.get(url_api)
    data = r.json()
    print(r.json())

    print(url_api)
    #data = request.get_json(url_api) #me va a devolver los datos que estoy enviando desde el cliente
    stat = data.get('status', None) #null para que no se rompa la applic
    url_image = data.get('message', None)
    print(stat)
    if stat:
        print('1')
        response = mongo.db.dogs.insert_one(
            {
                'breed': raza,
                'url': url_image,
                #'timestamp':,
                #'done': False
            }         
        )
        result = {
        #    'id': str(response.inserted_id),
        #    'datetime': str(response.inserted_id),
            'message': url_image,
            'Status': stat
        }
        return result
    else:
        return {'Breed is required', 400}


""""
def get_dogs_service():
    data = mongo.db.dogs.find() #estaria obteniendo los datos
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')
 
def get_dog_service(raza):
    #data = mongo.db.dogs.find_one({'_id': ObjectId(id)})
    #data = mongo.db.dogs.find_one({'_id': date(time)})
   
    data = mongo.db.dogs.find_one({'_id': ObjectId(id)})
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

"
def update_dog_service(id):
    data = request.get_json()
    if len(data) == 0:
        return {'Invalid Payload',400}
    
    response = mongo.db.dogs.update_one({'_id': ObjectId(id)}, {'$set':  data}) #entran todas las propiedades disponibles en data

    if response.modified_count >= 1:
        return 'Dog update succesfully', 200 #El código de estado HTTP 200 OK indica que una solicitud se realizó correctamente
    else:
        return 'Dog service not found', 404 #Se produce cuando un usuario intenta acceder a una URL que no existe en un sitio web
    
def delete_dog_service(id):
    response = mongo.db.dogs.delete._one({'_id': ObjectId(id)})
    if response.deleted_count >= 1:
        return 'Dog deleted succesfully',200
    else:
        return 'Dog not found', 404



def get_dogs_service():
    url = 'http://localhost:5000/dog/'
    #url = 'https://dog.ceo/api/breed/hound/images/random'
    response = request.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data  # Returns the JSON object directly as received from the API
    else:
        return {'message': 'Error', 'status': f'Error {response.status_code}: Unable to fetch image'}

# Example usage
hound_image = get_dogs_service()
print(hound_image)
"""




 



