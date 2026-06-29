# Raizes do Nordeste API - Trilha Back-End

Este projeto consiste em uma API RESTful desenvolvida em Python com FastAPI para o gerenciamento de pedidos de uma rede de alimentação. O sistema oferece funcionalidades de multicanalidade, controle de estoque, fidelidade e integração simulada (mock) de pagamentos, atendendo aos requisitos acadêmicos da disciplina de Projeto Multidisciplinar.

## Tecnologias Utilizadas
* Linguagem: Python 3.11+
* Framework: FastAPI
* Banco de Dados: PostgreSQL
* ORM: SQLAlchemy
* Containerização: Docker
* Validação: Pydantic

## Pré-requisitos
Antes de iniciar, certifique-se de ter as seguintes ferramentas instaladas em sua máquina:
* Git (para clonagem do repositório)
* Python 3.11 ou superior
* Docker Desktop (ou Docker Engine com Docker Compose)

## Guia de Execução

Siga os passos abaixo em seu terminal para configurar o ambiente e rodar o projeto:

### 1. Preparação
Certifique-se de que o Docker Desktop esteja aberto e em execução.

### 2. Instalação
```bash
# Clone o repositório e acesse a pasta
git clone <seu-link-aqui>
cd raizes-do-nordeste-api

# Crie e ative o ambiente virtual
python -m venv .venv
# No Windows:
.venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# 3. Suba o Banco de Dados PostgreSQL (O Docker precisa estar aberto)
docker compose up -d

# 4. Configure as Variáveis de Ambiente
# DICA: Crie uma cópia do arquivo '.env.example' e renomeie para '.env' na mesma pasta.

# 5. Inicie a API (As tabelas serão criadas automaticamente no banco de dados)
uvicorn app.main:app --reload
```

> **PASSO FINAL (SEED):** Com a API rodando no terminal acima, abra um **segundo terminal** na mesma pasta (com o `.venv` ativado) e execute o script abaixo para popular o banco de dados com os produtos de teste:
> ```bash
> python -m app.seed
> ```

---

## Documentação e Testes (Como avaliar)

* **Documentação Viva (Swagger):** Com a API no ar, acesse [http://localhost:8000/docs](http://localhost:8000/docs) para visualizar os contratos (requests/responses), permissões e endpoints.
* **Plano de Testes:** Na raiz deste repositório encontra-se o arquivo `raizes_do_nordeste_postman.json`. Importe este arquivo no seu **Postman**. A coleção já contém os 10 cenários de testes validados (6 positivos e 4 negativos), cobrindo todo o fluxo crítico: autenticação JWT, multicanalidade, baixa de estoque, LGPD e validação de erros padronizados.