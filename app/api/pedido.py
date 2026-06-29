from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app.core.deps import get_db, get_usuario_logado
from app.domain.item_pedido import ItemPedido
from app.domain.pedido import Pedido
from app.domain.produto import Produto
from app.schemas.item_pedido import ItemPedidoCreate
from app.schemas.pedido import PedidoCreate, PedidoResponse
import logging
from fastapi import status
from app.schemas.pedido import PedidoStatusUpdate

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - AUDITORIA - %(levelname)s - %(message)s"
)
logger = logging.getLogger("auditoria_pedidos")

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)


@router.get(
    "",
    response_model=list[PedidoResponse]
)
def listar_pedidos(
    canalPedido: Optional[str] = None,  # Parâmetro de query opcional
    db: Session = Depends(get_db)
):
    query = db.query(Pedido)
    
    if canalPedido:
        query = query.filter(Pedido.canal_pedido == canalPedido)
        
    return query.all()

@router.patch(
    "/{pedido_id}/status",
    response_model=PedidoResponse
)
def atualizar_status_pedido(
    pedido_id: int,
    dados: PedidoStatusUpdate,
    db: Session = Depends(get_db),
    usuario=Depends(get_usuario_logado)
):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")

    status_validos = ["AGUARDANDO_PAGAMENTO", "PAGO", "COZINHA", "PRONTO", "ENTREGUE", "CANCELADO"]
    if dados.status not in status_validos:
        raise HTTPException(
            status_code=422, 
            detail=f"Status inválido. Status permitidos: {', '.join(status_validos)}"
        )

    status_anterior = pedido.status
    pedido.status = dados.status
    
    db.commit()
    db.refresh(pedido)

    
    logger.info(f"Usuário {usuario['sub']} alterou o status do pedido {pedido.id} de '{status_anterior}' para '{pedido.status}'.")

    return pedido

@router.get(
    "/{pedido_id}",
    response_model=PedidoResponse
)
def buscar_pedido(
    pedido_id: int,
    db: Session = Depends(get_db)
):
    pedido = (
        db.query(Pedido)
        .filter(Pedido.id == pedido_id)
        .first()
    )

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado."
        )

    return pedido


@router.post(
    "",
    response_model=PedidoResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_pedido(
    dados: PedidoCreate,
    db: Session = Depends(get_db),
    usuario=Depends(get_usuario_logado)
):
    novo_pedido = Pedido(
        usuario_id=int(usuario["sub"]),
        canal_pedido=dados.canal_pedido,
        status="AGUARDANDO_PAGAMENTO",
        valor_total=0
    )

    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)
    logger.info(f"Usuário {usuario['sub']} CRIOU o pedido {novo_pedido.id} via canal {dados.canal_pedido}.")
    return novo_pedido
  


@router.post(
    "/{pedido_id}/itens"
)
def adicionar_item(
    pedido_id: int,
    dados: ItemPedidoCreate,
    db: Session = Depends(get_db),
    usuario=Depends(get_usuario_logado)
):
    pedido = (
        db.query(Pedido)
        .filter(Pedido.id == pedido_id)
        .first()
    )

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado."
        )

    if pedido.status == "PAGO":
        raise HTTPException(
            status_code=400,
            detail="Não é possível adicionar itens em um pedido pago."
        )

    produto = (
        db.query(Produto)
        .filter(Produto.id == dados.produto_id)
        .first()
    )

    if not produto:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    if produto.quantidade_estoque < dados.quantidade:
        raise HTTPException(
            status_code=409,
            detail="Estoque insuficiente."
        )

    item = ItemPedido(
        pedido_id=pedido.id,
        produto_id=produto.id,
        quantidade=dados.quantidade
    )

    db.add(item)

    produto.quantidade_estoque -= dados.quantidade

    pedido.valor_total += produto.preco * dados.quantidade

    db.commit()

    return {
        "mensagem": "Item adicionado ao pedido."
    }


@router.post(
    "/{pedido_id}/pagamento",
    response_model=PedidoResponse
)
def pagar_pedido(
    pedido_id: int,
    db: Session = Depends(get_db),
    usuario=Depends(get_usuario_logado)
):
    pedido = (
        db.query(Pedido)
        .filter(Pedido.id == pedido_id)
        .first()
    )

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado."
        )

    if pedido.status == "PAGO":
        raise HTTPException(
            status_code=400,
            detail="Pedido já foi pago."
        )

    pedido.status = "PAGO"

    db.commit()
    db.refresh(pedido)
   
    logger.info(f"Usuário {usuario['sub']} PAGOU o pedido {pedido.id}.")
    return pedido
   