from flask import Blueprint, jsonify, request
from app.controllers import categoria_controller as controller

bp_categorias = Blueprint('categorias', __name__, url_prefix='/categorias')

@bp_categorias.route('/', methods=['GET'])
def listar():
    """
    Lista todas as categorias
    ---
    tags:
      - Categorias
    responses:
      200:
        description: Lista de categorias
        examples:
          application/json: [
            {
              "id": 1,
              "nome": "Eletrônicos",
              "descricao": "Dispositivos eletrônicos",
              "codigo": "ELEC"
            }
          ]
    """
    categorias = controller.listar_categorias()
    return jsonify([c.to_dict() for c in categorias])

@bp_categorias.route('/<int:id>', methods=['GET'])
def obter(id):
    """
    Retorna uma categoria específica pelo ID
    ---
    tags:
      - Categorias
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da categoria
    responses:
      200:
        description: Categoria encontrada
        examples:
          application/json:
            {
              "id": 1,
              "nome": "Eletrônicos",
              "descricao": "Dispositivos eletrônicos",
              "codigo": "ELEC"
            }
      404:
        description: Categoria não encontrada
    """
    c = controller.obter_categoria(id)
    return jsonify(c.to_dict()) if c else ('', 404)

@bp_categorias.route('/', methods=['POST'])
def criar():
    """
    Cria uma nova categoria
    ---
    tags:
      - Categorias
    requestBody:
      required: true
      content:
        application/json:
          example:
            {
              "nome": "Livros",
              "descricao": "Livros e revistas",
              "codigo": "LIVR"
            }
    responses:
      201:
        description: Categoria criada com sucesso
        examples:
          application/json:
            {
              "id": 2,
              "nome": "Livros",
              "descricao": "Livros e revistas",
              "codigo": "LIVR"
            }
    """
    c = controller.criar_categoria(request.json)
    return jsonify(c.to_dict()), 201

@bp_categorias.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    """
    Atualiza uma categoria existente
    ---
    tags:
      - Categorias
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da categoria
    requestBody:
      required: true
      content:
        application/json:
          example:
            {
              "nome": "Eletrônicos e Gadgets",
              "descricao": "Atualizado",
              "codigo": "ELECGAD"
            }
    responses:
      200:
        description: Categoria atualizada com sucesso
        examples:
          application/json:
            {
              "id": 1,
              "nome": "Eletrônicos e Gadgets",
              "descricao": "Atualizado",
              "codigo": "ELECGAD"
            }
      404:
        description: Categoria não encontrada
    """
    c = controller.atualizar_categoria(id, request.json)
    return jsonify(c.to_dict()) if c else ('', 404)

@bp_categorias.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    """
    Deleta uma categoria pelo ID
    ---
    tags:
      - Categorias
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da categoria
    responses:
      200:
        description: Categoria deletada com sucesso
        examples:
          application/json:
            { "deleted": true }
      404:
        description: Categoria não encontrada
    """
    c = controller.deletar_categoria(id)
    return jsonify({ 'deleted': True }) if c else ('', 404)