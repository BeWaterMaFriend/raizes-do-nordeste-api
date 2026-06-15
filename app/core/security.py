from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def gerar_hash(senha: str):
    return pwd_context.hash(senha)


def verificar_senha(senha: str, senha_hash: str):
    return pwd_context.verify(senha, senha_hash)


def criar_token_acesso(dados: dict):
    payload = dados.copy()
    expira = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp": expira})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)