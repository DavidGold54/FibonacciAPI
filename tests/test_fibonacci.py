import pytest
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

@pytest.mark.parametrize("n, expected_result", [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55),
    (99, 218922995834555169026)
])
def test_get_fibonacci_success(n, expected_result):
    response = client.get(f"/api/v1/fib?n={n}")
    assert response.status_code == 200
    assert response.json() == {"result": expected_result}

@pytest.mark.parametrize("n", [-1, 0])
def test_get_fibonacci_bad_request(n):
    response = client.get(f"/api/v1/fib?n={n}")
    assert response.status_code == 400

@pytest.mark.parametrize("n", ["abc", 'a', None, 1.5, -0.1, True, [1], (1, 2)])
def test_get_fibonacci_non_integer_input(n):
    response = client.get(f"/api/v1/fib?n={n}")
    assert response.status_code == 422