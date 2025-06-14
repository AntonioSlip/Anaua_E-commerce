from flask import Flask
from flasgger import Swagger
from app.models import db
from .routes.Produto_routes import bp_produtos
from .routes.Categoria_routes import bp_categorias
from .routes.Usuario_routes import bp_usuarios
from .routes.Venda_routes import bp_vendas
from .routes.ItemVenda_routes import bp_itens_venda

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anaua.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Swagger(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(bp_produtos)
    app.register_blueprint(bp_categorias)
    app.register_blueprint(bp_usuarios)
    app.register_blueprint(bp_vendas)
    app.register_blueprint(bp_itens_venda)

    return app