from flask import Blueprint, jsonify, request
from app.controllers import usuario_controller as controller

bp_usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@bp_usuarios.route('/', methods=['GET'])
def listar():
    """
    Lista todos os usuários
    ---
    tags:
      - Usuários
    responses:
      200:
        description: Lista de usuários
        examples:
          application/json: [
            {
              "id": 1,
              "nome": "João Silva",
              "email": "joao@example.com",
              "endereco": "Rua A, 123",
              "telefone": "(11) 99999-9999",
              "is_admin": false
            }
          ]
    """
    usuarios = controller.listar_usuarios()
    return jsonify([u.to_dict() for u in usuarios])

@bp_usuarios.route('/<int:id>', methods=['GET'])
def obter(id):
    """
    Retorna um usuário específico pelo ID
    ---
    tags:
      - Usuários
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do usuário
    responses:
      200:
        description: Usuário encontrado
        examples:
          application/json:
            {
              "id": 1,
              "nome": "João Silva",
              "email": "joao@example.com",
              "endereco": "Rua A, 123",
              "telefone": "(11) 99999-9999",
              "is_admin": false
            }
      404:
        description: Usuário não encontrado
    """
    u = controller.obter_usuario(id)
    return jsonify(u.to_dict()) if u else ('', 404)

@bp_usuarios.route('/', methods=['POST'])
def criar():
    """
    Cria um novo usuário
    ---
    tags:
      - Usuários
    requestBody:
      required: true
      content:
        application/json:
          example:
            {
              "nome": "Maria Oliveira",
              "email": "maria@example.com",
              "senha_hash": "senha123",  # (obs: normalmente seria hash, mas aqui é direto)
              "endereco": "Rua B, 456",
              "telefone": "(21) 88888-8888",
              "is_admin": false
            }
    responses:
      201:
        description: Usuário criado com sucesso
        examples:
          application/json:
            {
              "id": 2,
              "nome": "Maria Oliveira",
              "email": "maria@example.com",
              "endereco": "Rua B, 456",
              "telefone": "(21) 88888-8888",
              "is_admin": false
            }
    """
    u = controller.criar_usuario(request.json)
    return jsonify(u.to_dict()), 201

@bp_usuarios.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    """
    Atualiza um usuário existente
    ---
    tags:
      - Usuários
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do usuário
    requestBody:
      required: true
      content:
        application/json:
          example:
            {
              "nome": "João Atualizado",
              "email": "joao_novo@example.com",
              "endereco": "Rua Nova, 789",
              "telefone": "(31) 77777-7777",
              "is_admin": true
            }
    responses:
      200:
        description: Usuário atualizado com sucesso
        examples:
          application/json:
            {
              "id": 1,
              "nome": "João Atualizado",
              "email": "joao_novo@example.com",
              "endereco": "Rua Nova, 789",
              "telefone": "(31) 77777-7777",
              "is_admin": true
            }
      404:
        description: Usuário não encontrado
    """
    u = controller.atualizar_usuario(id, request.json)
    return jsonify(u.to_dict()) if u else ('', 404)

@bp_usuarios.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    """
    Deleta um usuário pelo ID
    ---
    tags:
      - Usuários
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do usuário
    responses:
      200:
        description: Usuário deletado com sucesso
        examples:
          application/json:
            { "deleted": true }
      404:
        description: Usuário não encontrado
    """
    u = controller.deletar_usuario(id)
    return jsonify({ 'deleted': True }) if u else ('', 404)