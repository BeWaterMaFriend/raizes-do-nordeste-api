from pydantic import BaseModel


class ItemPedidoCreate(BaseModel):
    produto_id: int
    quantidade: int


class ItemPedidoResponse(BaseModel):
    id: int
    pedido_id: int
    produto_id: int
    quantidade: int

    class Config:
        from_attributes = True