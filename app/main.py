from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.routes import router


app = FastAPI(
    title="Fibonacci API",
    version="1.0.0",
    description="An API to calculate Fibonacci numbers",
)

app.include_router(router, prefix="/api/v1")

@app.get("/", response_class=JSONResponse)
def read_root() -> JSONResponse:
    content = {"message": "Welcome to the Fibonacci API"}
    return JSONResponse(content)