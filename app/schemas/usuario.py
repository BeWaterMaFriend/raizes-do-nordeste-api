from pydantic import BaseModel, EmailStr


class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    perfil: str


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    perfil: str

    class Config:
        from_attributes = True