from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from jwt_utility import generate_jwt, validate_jwt
from os import environ

app = FastAPI()

SECRET_KEY = environ["JWT_SECRET"]


class GenerateJWTRequest(BaseModel):
    data: str


@app.post("/generate-jwt")
async def generate_jwt_endpoint(request: GenerateJWTRequest):
    jwt_token = generate_jwt(request.data, SECRET_KEY)
    return {"jwt": jwt_token}


@app.get("/validate-jwt/{jwt_token}")
async def validate_jwt_endpoint(jwt_token: str):
    validation_result = validate_jwt(jwt_token, SECRET_KEY)

    if isinstance(validation_result, str):
        raise HTTPException(status_code=400, detail=validation_result)

    return {"payload": validation_result}
