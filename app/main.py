from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from datetime import datetime, timezone

from app.api.pedido import router as pedido_router
from app.core.database import engine
from app.domain.base import Base
from app.api.auth import router as auth_router
from app.api.teste import router as teste_router
from app.api.produto import router as produto_router

app = FastAPI(
    title="Raízes do Nordeste API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

# ==========================================
# EXCEPTION HANDLERS (PADRÃO DE ERRO EXIGIDO)
# ==========================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    # Mapeia o status code para um nome de erro legível
    error_mapping = {
        400: "BAD_REQUEST",
        401: "UNAUTHORIZED",
        403: "FORBIDDEN",
        404: "NOT_FOUND",
        409: "CONFLICT",
        422: "UNPROCESSABLE_ENTITY"
    }
    error_name = error_mapping.get(exc.status_code, "ERROR")

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": error_name,
            "message": exc.detail,
            "details": [],
            "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "path": request.url.path
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Extrai os detalhes do erro do Pydantic no formato exigido
    details = [{"field": ".".join(map(str, err["loc"])), "issue": err["msg"]} for err in exc.errors()]
    
    return JSONResponse(
        status_code=422,
        content={
            "error": "UNPROCESSABLE_ENTITY",
            "message": "Erro de validação dos dados enviados.",
            "details": details,
            "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "path": request.url.path
        }
    )

# ==========================================
# ROTAS
# ==========================================

app.include_router(auth_router)
app.include_router(teste_router)
app.include_router(produto_router)
app.include_router(pedido_router)

@app.get("/")
def root():
    return {"message": "API funcionando"}