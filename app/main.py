from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="Fibonacci API",
    version="1.0.0",
    description="An API to calculate Fibonacci numbers",
)

app.include_router(router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fibonacci API"}