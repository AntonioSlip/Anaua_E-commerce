from app.models import Categoria, db

def listar_categorias():
    return Categoria.query.all()

def obter_categoria(id):
    return Categoria.query.get(id)

def criar_categoria(data):
    categoria = Categoria(**data)
    db.session.add(categoria)
    db.session.commit()
    return categoria

def atualizar_categoria(id, data):
    categoria = Categoria.query.get(id)
    if not categoria:
        return None
    for key, value in data.items():
        setattr(categoria, key, value)
    db.session.commit()
    return categoria

def deletar_categoria(id):
    categoria = Categoria.query.get(id)
    if not categoria:
        return None
    db.session.delete(categoria)
    db.session.commit()
    return categoria
