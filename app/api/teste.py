from fastapi import APIRouter, Depends

from app.core.deps import get_usuario_logado

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