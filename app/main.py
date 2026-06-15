from fastapi import FastAPI

from app.core.database import engine
from app.domain.base import Base
from app.domain.usuario import Usuario

app = FastAPI(
    title="Raízes do Nordeste API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API funcionando"}