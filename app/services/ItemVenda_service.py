from app.models import ItemVenda, db

def listar_itens():
    return ItemVenda.query.all()

def obter_item(id):
    return ItemVenda.query.get(id)

def criar_item(data):
    item = ItemVenda(**data)
    db.session.add(item)
    db.session.commit()
    return item

def atualizar_item(id, data):
    item = ItemVenda.query.get(id)
    if not item:
        return None
    for key, value in data.items():
        setattr(item, key, value)
    db.session.commit()
    return item

def deletar_item(id):
    item = ItemVenda.query.get(id)
    if not item:
        return None
    db.session.delete(item)
    db.session.commit()
    return item