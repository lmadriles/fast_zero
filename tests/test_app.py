from http import HTTPStatus
  
from fastapi.testclient import TestClient
 
from fast_duno.app import app
  

def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # arrange (setando o teste)

    response = client.get('/')  # act (chama a função no teste)

    # assert (garanta que):
    assert response.status_code == HTTPStatus.OK  # testa se ok
    # sendo HTTPStatus.OK = 200
    assert response.json() == {'message': 'Hello World'}
    # testa se a mensagem está sendo exibida corretamente