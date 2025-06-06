from app.models import Produto, db

def listar_produtos():
    return Produto.query.all()

def obter_produto(produto_id):
    return Produto.query.get(produto_id)

def criar_produto(data):
    produto = Produto(
        nome=data['nome'],
        descricao=data.get('descricao', ''),
        preco=data['preco'],
        estoque=data.get('estoque', 0),
        foto_url=data.get('foto_url', ''),
        categoria_id=data.get('categoria_id')
    )
    db.session.add(produto)
    db.session.commit()
    return produto

def atualizar_produto(produto_id, data):
    produto = Produto.query.get(produto_id)
    if not produto:
        return None
    produto.nome = data.get('nome', produto.nome)
    produto.descricao = data.get('descricao', produto.descricao)
    produto.preco = data.get('preco', produto.preco)
    produto.estoque = data.get('estoque', produto.estoque)
    produto.foto_url = data.get('foto_url', produto.foto_url)
    produto.categoria_id = data.get('categoria_id', produto.categoria_id)
    db.session.commit()
    return produto

def deletar_produto(produto_id):
    produto = Produto.query.get(produto_id)
    if not produto:
        return None
    db.session.delete(produto)
    db.session.commit()
    return produto
