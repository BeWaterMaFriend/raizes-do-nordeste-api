# Raízes do Nordeste API

Projeto desenvolvido para a disciplina de Arquitetura de Software.

## Tecnologias

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker
- JWT
- Swagger/OpenAPI

## Como executar

### Criar ambiente virtual

```bash
python -m venv .venv
```

### Ativar ambiente

Windows:

```bash
.venv\Scripts\activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Subir PostgreSQL

```bash
docker compose up -d
```

### Executar API

```bash
uvicorn app.main:app --reload
```

Swagger:

```text
http://localhost:8000/docs
```