from fastapi import FastAPI

from app.core.database import engine
from app.domain.base import Base
from app.domain.usuario import Usuario
from app.api.auth import router as auth_router
from app.api.teste import router as teste_router

app = FastAPI(
    title="Raízes do Nordeste API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(teste_router)


@app.get("/")
def root():
    return {"message": "API funcionando"}