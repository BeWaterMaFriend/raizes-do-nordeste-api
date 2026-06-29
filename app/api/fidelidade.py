from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_cliente
from app.domain.usuario import Usuario

router = APIRouter(
    prefix="/fidelidade",
    tags=["Fidelidade"]
)

@router.get("/saldo")
def consultar_saldo(
    db: Session = Depends(get_db),
    usuario=Depends(get_cliente) # Apenas clientes logados podem ver os pontos
):
    cliente = db.query(Usuario).filter(Usuario.id == int(usuario["sub"])).first()
    
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
        
    return {
        "usuario_id": cliente.id,
        "nome": cliente.nome,
        "pontos_fidelidade": cliente.pontos_fidelidade,
        "mensagem_lgpd": "Seus dados são processados conforme os termos aceitos (LGPD)."
    }