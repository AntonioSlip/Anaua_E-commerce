from .Base import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)
    endereco = db.Column(db.String(200))
    telefone = db.Column(db.String(20))
    is_admin = db.Column(db.Boolean, default=False)
    vendas = db.relationship('Venda', backref='usuario', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'endereco': self.endereco,
            'telefone': self.telefone,
            'is_admin': self.is_admin
        }
