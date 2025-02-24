from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()

class TextRequest(BaseModel):
    text: str

def vectorize(text: str):
    # Пример векторизации: преобразует каждый символ в его ASCII-код
    vector = np.array([ord(ch) for ch in text])
    return vector

@app.post("/vectorize")
async def vectorize_text(request: TextRequest):
    vector = vectorize(request.text)
    return {"vector": vector.tolist()}

@app.get("/")
async def read_root():
    return {"message": "FastAPI работает"}
