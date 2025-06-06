from app.models import Usuario, db

def listar_usuarios():
    return Usuario.query.all()

def obter_usuario(id):
    return Usuario.query.get(id)

def criar_usuario(data):
    usuario = Usuario(**data)
    db.session.add(usuario)
    db.session.commit()
    return usuario

def atualizar_usuario(id, data):
    usuario = Usuario.query.get(id)
    if not usuario:
        return None
    for key, value in data.items():
        setattr(usuario, key, value)
    db.session.commit()
    return usuario

def deletar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return None
    db.session.delete(usuario)
    db.session.commit()
    return usuario