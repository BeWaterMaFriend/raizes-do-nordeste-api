from sqlalchemy import String, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.base import Base


class Produto(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(100))

    descricao: Mapped[str] = mapped_column(String(255))

    preco: Mapped[float] = mapped_column(Float)

    ativo: Mapped[bool] = mapped_column(Boolean, default=True)

    quantidade_estoque: Mapped[int] = mapped_column(default=0)