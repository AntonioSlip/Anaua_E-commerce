from flask import Blueprint
from app.controllers import Categoria_controller

bp_categorias = Blueprint('categorias', __name__, url_prefix='/categorias')

bp_categorias.route('/', methods=['GET'])(Categoria_controller.listar_categorias)
bp_categorias.route('/<int:id>', methods=['GET'])(Categoria_controller.obter_categoria)
bp_categorias.route('/', methods=['POST'])(Categoria_controller.criar_categoria)
bp_categorias.route('/<int:id>', methods=['PUT'])(Categoria_controller.atualizar_categoria)
bp_categorias.route('/<int:id>', methods=['DELETE'])(Categoria_controller.deletar_categoria)
