# Raízes do Nordeste API - Trilha Back-End

Projeto desenvolvido em FastAPI para gestão de pedidos multicanal (App, Totem, Balcão), atendendo a todos os requisitos do Projeto Multidisciplinar.

---

## Guia Rápido de Execução

Siga os passos abaixo no seu terminal para configurar, instalar e rodar o projeto do zero:

```bash
# 1. Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate

# 2. Instale as dependências da API
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
> python app/seed.py
> ```

---

## Documentação e Testes (Como avaliar)

* **Documentação Viva (Swagger):** Com a API no ar, acesse [http://localhost:8000/docs](http://localhost:8000/docs) para visualizar os contratos (requests/responses), permissões e endpoints.
* **Plano de Testes:** Na raiz deste repositório encontra-se o arquivo `raizes_do_nordeste_postman.json`. Importe este arquivo no seu **Postman**. A coleção já contém os 10 cenários de testes validados (6 positivos e 4 negativos), cobrindo todo o fluxo crítico: autenticação JWT, multicanalidade, baixa de estoque, LGPD e validação de erros padronizados.