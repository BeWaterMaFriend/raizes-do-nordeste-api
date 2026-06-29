from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.domain.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(150), unique=True)
    senha_hash: Mapped[str] = mapped_column(String(255))
    tipo_usuario: Mapped[str] = mapped_column(String(20))
    
    # NOVOS CAMPOS: LGPD e Fidelidade
    aceite_termos_lgpd: Mapped[bool] = mapped_column(Boolean, default=False)
    pontos_fidelidade: Mapped[int] = mapped_column(Integer, default=0)