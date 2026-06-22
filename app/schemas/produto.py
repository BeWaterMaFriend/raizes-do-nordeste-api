from pydantic import BaseModel, ConfigDict


class ProdutoCreate(BaseModel):
    nome: str
    descricao: str
    preco: float
    ativo: bool = True


class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    ativo: bool

    model_config = ConfigDict(from_attributes=True)