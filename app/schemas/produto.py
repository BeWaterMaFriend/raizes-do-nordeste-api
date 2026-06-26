from pydantic import BaseModel, ConfigDict


class ProdutoCreate(BaseModel):
    nome: str
    descricao: str
    preco: float
    ativo: bool = True
    quantidade_estoque: int


class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    ativo: bool
    quantidade_estoque: int

    model_config = ConfigDict(
        from_attributes=True
    )


class ProdutoUpdate(BaseModel):
    nome: str
    descricao: str
    preco: float
    ativo: bool
    quantidade_estoque: int