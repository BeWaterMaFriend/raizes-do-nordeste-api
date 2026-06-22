from fastapi import APIRouter, Depends

from app.core.deps import (
    get_usuario_logado,
    get_admin,
    get_cliente
)

router = APIRouter(
    prefix="/teste",
    tags=["Teste"]
)


@router.get("/privado")
def rota_privada(
    usuario=Depends(get_usuario_logado)
):
    return {
        "mensagem": "Token válido",
        "usuario": usuario
    }


@router.get("/admin")
def rota_admin(
    usuario=Depends(get_admin)
):
    return {
        "mensagem": "Área ADMIN",
        "usuario": usuario
    }


@router.get("/cliente")
def rota_cliente(
    usuario=Depends(get_cliente)
):
    return {
        "mensagem": "Área CLIENTE",
        "usuario": usuario
    }