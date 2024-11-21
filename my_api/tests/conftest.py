#TUTO FROM: https://www.youtube.com/watch?v=bjvCr3Y_zN0

import pytest
from app import app as flask_app

import requests #antes de ver si es necesario request de flask

"""
def test_breeds() -> None:
    response = requests.get('http://localhost:5000/dog/breed/houndm', timeout=3)
    assert response.status_code == 300 #el esperado es
"""
def test_breeds() -> None:
    response = requests.get('http://localhost:5000/dog/breed/hound', timeout=3)
    assert response.status_code == 200

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_client(client):
    response = client.get('/dog/breed/houndm')
    assert response.status_code == 200

#Este archivo inicializará nuestra aplic flask y todos los dispositivos que necesita
#además podemos relizar cualquier personalización sobre el cliente/app que necesitemos
#como pasar a modo de pruebas, cambiar la base de datos, etc.


