from typing import Any

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
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (99, 218922995834555169026)
])
def test_get_fibonacci_success(n: Any, expected_result: Any) -> None:
    response = client.get(f"/api/v1/fib?n={n}")
    assert response.status_code == 200
    assert response.content == ('{"result":'+str(expected_result)+'}').encode()

@pytest.mark.parametrize("n", [
    0,
    -1,
    -100,
    1.5,
    -1.5,
    "a",
    "abc",
    "123a",
    "b456",
    True,
    None,
    [10],
    (1, 2, 3)
])
def test_get_fibonacci_bad_request(n: Any) -> None:
    response = client.get(f"/api/v1/fib?n={n}")
    assert response.status_code == 400
    assert response.content == '{"status":400,"message":"Bad request."}'.encode()
