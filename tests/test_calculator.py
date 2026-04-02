from app.calculator import sum, resta, mul
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Pruebas unitarias
def test_sum() -> None:
    assert sum(2, 3) == 5

def test_resta() -> None:
    assert resta(5, 3) == 2

def test_multiply() -> None:
    assert mul(2, 3) == 6

# Pruebas de endpoints
def test_endpoint_suma() -> None:
    response = client.post("/suma", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"operacion": "suma", "a": 2, "b": 3, "resultado": 5}

def test_endpoint_resta() -> None:
    response = client.post("/resta", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"operacion": "resta", "a": 5, "b": 3, "resultado": 2}

def test_endpoint_multiplicacion() -> None:
    response = client.post("/multiplicacion", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"operacion": "multiplicacion", "a": 2, "b": 3, "resultado": 6}

def test_endpoint_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "mensaje" in response.json()