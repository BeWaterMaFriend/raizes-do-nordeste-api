from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.base import Base


class Pedido(Base):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(primary_key=True)

    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id")
    )

    canal_pedido: Mapped[str] = mapped_column(
        String(30)
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="AGUARDANDO_PAGAMENTO"
    )

    valor_total: Mapped[float] = mapped_column(
        Float,
        default=0
    )