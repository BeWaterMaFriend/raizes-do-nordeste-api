from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.base import Base


class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id: Mapped[int] = mapped_column(primary_key=True)

    pedido_id: Mapped[int] = mapped_column(
        ForeignKey("pedidos.id")
    )

    produto_id: Mapped[int] = mapped_column(
        ForeignKey("produtos.id")
    )

    quantidade: Mapped[int] = mapped_column()