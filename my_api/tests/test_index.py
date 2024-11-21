import json #para evaluar la respuesta

"""
def test_index(app, client):
    response =client.get('/breed/<raza>')
    assert response.status_code == 200
"""
#improved:
def test_index(app, client):
    raza = 'golden'
    response = client.get(f'/breed/{raza}')
    assert response.status_code == 200
    assert response.json() == {'message': f'Breed: {raza}'}

#En la terminal:    
#   > pytest my_api/tests/test_index.py
    
    