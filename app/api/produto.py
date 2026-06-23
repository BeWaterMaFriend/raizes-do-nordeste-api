from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_admin
from app.domain.produto import Produto
from app.schemas.produto import (
    ProdutoCreate,
    ProdutoResponse
)

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)


@router.get(
    "",
    response_model=list[ProdutoResponse]
)
def listar_produtos(
    db: Session = Depends(get_db)
):
    return db.query(Produto).all()


@router.post(
    "",
    response_model=ProdutoResponse
)
def criar_produto(
    produto: ProdutoCreate,
    db: Session = Depends(get_db),
    usuario=Depends(get_admin)
):
    novo_produto = Produto(
        nome=produto.nome,
        descricao=produto.descricao,
        preco=produto.preco,
        ativo=produto.ativo
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto