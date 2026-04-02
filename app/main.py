from fastapi import FastAPI
from pydantic import BaseModel
from app.calculator import sum, resta, mul

app = FastAPI(title="Calculator API")

class CalcRequest(BaseModel):
    a: int
    b: int

@app.post("/suma")
def endpoint_suma(request: CalcRequest) -> dict:
    """Endpoint para suma"""
    result = sum(request.a, request.b)
    return {"operacion": "suma", "a": request.a, "b": request.b, "resultado": result}

@app.post("/resta")
def endpoint_resta(request: CalcRequest) -> dict:
    """Endpoint para resta"""
    result = resta(request.a, request.b)
    return {"operacion": "resta", "a": request.a, "b": request.b, "resultado": result}

@app.post("/multiplicacion")
def endpoint_multiplicacion(request: CalcRequest) -> dict:
    """Endpoint para multiplicacion"""
    result = mul(request.a, request.b)
    return {"operacion": "multiplicacion", "a": request.a, "b": request.b, "resultado": result}

@app.get("/")
def root() -> dict:
    """Endpoint raiz"""
    return {"mensaje": "Calculator API - Endpoints: /suma, /resta, /multiplicacion"}
