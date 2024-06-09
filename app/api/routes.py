from fastapi import APIRouter, HTTPException, status

from app.models.response import Response
from app.services.fibonacci import calculate_fibonacci
from app.utils.validators import validate_positive_integer


router = APIRouter()

@router.get("/fib", response_model=Response, status_code=status.HTTP_200_OK)
def get_fibonacci(n: int):
    try:
        n = validate_positive_integer(n)
        result = calculate_fibonacci(n)
        return Response(result=result)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
