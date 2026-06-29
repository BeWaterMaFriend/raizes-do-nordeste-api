from pydantic import BaseModel


class PedidoCreate(BaseModel):
    canal_pedido: str


class PedidoResponse(BaseModel):
    id: int
    usuario_id: int
    canal_pedido: str
    status: str
    valor_total: float

    class Config:
        from_attributes = True

class PedidoStatusUpdate(BaseModel):
    status: str