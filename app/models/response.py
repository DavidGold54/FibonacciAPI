from pydantic import BaseModel


class Response(BaseModel):
    result: int