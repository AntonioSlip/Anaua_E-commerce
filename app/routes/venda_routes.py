from flask import Blueprint
from app.controllers import Venda_controller

bp_vendas = Blueprint('vendas', __name__, url_prefix='/vendas')

bp_vendas.route('/', methods=['GET'])(Venda_controller.listar)
bp_vendas.route('/<int:id>', methods=['GET'])(Venda_controller.obter)
bp_vendas.route('/', methods=['POST'])(Venda_controller.criar)
bp_vendas.route('/<int:id>', methods=['PUT'])(Venda_controller.atualizar)
bp_vendas.route('/<int:id>', methods=['DELETE'])(Venda_controller.deletar)
