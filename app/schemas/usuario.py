from pydantic import BaseModel, EmailStr

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    perfil: str
    aceite_termos_lgpd: bool # O usuário tem que consentir no momento do cadastro

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    perfil: str
    pontos_fidelidade: int # Mostramos os pontos na resposta

    class Config:
        from_attributes = True