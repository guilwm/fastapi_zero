from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Este teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act - Ação
    - A: Assert - Afirmação
    """

    client = TestClient(app)

    response = client.get('/')
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK

def test_root_deve_retornar_html():
    
    client = TestClient(app)

    response = client.get('/items/{item_id}')
    print(response.text)
    assert response.status_code == HTTPStatus.OK
    assert "<h1>Olá Mundo!</h1>" in response.text 
