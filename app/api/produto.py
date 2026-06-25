from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_admin
from app.domain.produto import Produto
from app.schemas.produto import (
    ProdutoCreate,
    ProdutoUpdate,
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

@router.get(
    "/{produto_id}",
    response_model=ProdutoResponse
)
def buscar_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):
    produto = (
        db.query(Produto)
        .filter(Produto.id == produto_id)
        .first()
    )

    if not produto:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    return produto

@router.put(
    "/{produto_id}",
    response_model=ProdutoResponse
)
def atualizar_produto(
    produto_id: int,
    dados: ProdutoUpdate,
    db: Session = Depends(get_db),
    usuario=Depends(get_admin)
):
    produto = (
        db.query(Produto)
        .filter(Produto.id == produto_id)
        .first()
    )

    if not produto:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    produto.nome = dados.nome
    produto.descricao = dados.descricao
    produto.preco = dados.preco
    produto.ativo = dados.ativo

    db.commit()
    db.refresh(produto)

    return produto

@router.delete(
    "/{produto_id}"
)
def excluir_produto(
    produto_id: int,
    db: Session = Depends(get_db),
    usuario=Depends(get_admin)
):
    produto = (
        db.query(Produto)
        .filter(Produto.id == produto_id)
        .first()
    )

    if not produto:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    db.delete(produto)
    db.commit()

    return {
        "mensagem": "Produto removido com sucesso."
    }

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