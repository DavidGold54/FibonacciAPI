from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.fibonacci import calculate_fibonacci
from app.utils.validators import validate_positive_integer


router = APIRouter()

@router.get("/fib", response_class=JSONResponse)
def get_fibonacci(n: str) -> JSONResponse:
    try:
        n = validate_positive_integer(n)
        content = {"result": calculate_fibonacci(n)}
        return JSONResponse(content, status_code=200)
    except ValueError:
        content = {"status": 400, "message": "Bad request."}
        return JSONResponse(content, status_code=400)
