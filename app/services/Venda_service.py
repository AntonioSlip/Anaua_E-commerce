from app.models import Venda, db

def listar_vendas():
    return Venda.query.all()

def obter_venda(id):
    return Venda.query.get(id)

def criar_venda(data):
    venda = Venda(**data)
    db.session.add(venda)
    db.session.commit()
    return venda

def atualizar_venda(id, data):
    venda = Venda.query.get(id)
    if not venda:
        return None
    for key, value in data.items():
        setattr(venda, key, value)
    db.session.commit()
    return venda

def deletar_venda(id):
    venda = Venda.query.get(id)
    if not venda:
        return None
    db.session.delete(venda)
    db.session.commit()
    return venda
