from flask import Blueprint
from app.controllers import Usuario_controller

bp_usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios')

bp_usuarios.route('/', methods=['GET'])(Usuario_controller.listar)
bp_usuarios.route('/<int:id>', methods=['GET'])(Usuario_controller.obter)
bp_usuarios.route('/', methods=['POST'])(Usuario_controller.criar)
bp_usuarios.route('/<int:id>', methods=['PUT'])(Usuario_controller.atualizar)
bp_usuarios.route('/<int:id>', methods=['DELETE'])(Usuario_controller.deletar)
