from app.core.database import SessionLocal
from app.domain.produto import Produto

db = SessionLocal()

produtos_iniciais = [
    Produto(nome="Hambúrguer Sertanejo", descricao="Blend de carne de sol com queijo coalho", preco=35.90, quantidade_estoque=50),
    Produto(nome="Porção de Macaxeira", descricao="Macaxeira frita crocante", preco=15.50, quantidade_estoque=100),
    Produto(nome="Refrigerante Cajuína", descricao="Cajuína regional 350ml", preco=7.00, quantidade_estoque=200)
]

for p in produtos_iniciais:
    if not db.query(Produto).filter(Produto.nome == p.nome).first():
        db.add(p)

db.commit()
print("Banco de dados populado com produtos iniciais de sucesso!")