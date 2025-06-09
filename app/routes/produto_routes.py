from flask import Blueprint
from app.controllers import Produto_controller

bp_produtos = Blueprint('produtos', __name__, url_prefix='/produtos')

bp_produtos.route('/', methods=['GET'])(Produto_controller.get_all)
bp_produtos.route('/<int:produto_id>', methods=['GET'])(Produto_controller.get_one)
bp_produtos.route('/', methods=['POST'])(Produto_controller.create)
bp_produtos.route('/<int:produto_id>', methods=['PUT'])(Produto_controller.update)
bp_produtos.route('/<int:produto_id>', methods=['DELETE'])(Produto_controller.delete)
