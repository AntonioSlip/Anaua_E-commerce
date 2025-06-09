from flask import Blueprint
from app.controllers import ItemVenda_controller

bp_itens_venda = Blueprint('itens_venda', __name__, url_prefix='/itens-venda')

bp_itens_venda.route('/', methods=['GET'])(ItemVenda_controller.listar)
bp_itens_venda.route('/<int:id>', methods=['GET'])(ItemVenda_controller.obter)
bp_itens_venda.route('/', methods=['POST'])(ItemVenda_controller.criar)
bp_itens_venda.route('/<int:id>', methods=['PUT'])(ItemVenda_controller.atualizar)
bp_itens_venda.route('/<int:id>', methods=['DELETE'])(ItemVenda_controller.deletar)
