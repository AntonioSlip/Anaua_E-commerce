from flask import Blueprint, jsonify, request
from app.controllers import itemvenda_controller as controller

bp_itens_venda = Blueprint('itens_venda', __name__, url_prefix='/itens-venda')

@bp_itens_venda.route('/', methods=['GET'])
def listar():
    """
    Lista todos os itens de venda
    ---
    tags:
      - Itens de Venda
    responses:
      200:
        description: Lista de itens de venda
        examples:
          application/json: [
            {
              "id": 1,
              "venda_id": 3,
              "produto_id": 5,
              "quantidade": 2,
              "preco_unitario": 50.0
            }
          ]
    """
    itens = controller.listar_itens()
    return jsonify([i.__dict__ for i in itens])

@bp_itens_venda.route('/<int:id>', methods=['GET'])
def obter(id):
    """
    Retorna um item de venda específico pelo ID
    ---
    tags:
      - Itens de Venda
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do item de venda
    responses:
      200:
        description: Item de venda encontrado
        examples:
          application/json:
            {
              "id": 1,
              "venda_id": 3,
              "produto_id": 5,
              "quantidade": 2,
              "preco_unitario": 50.0
            }
      404:
        description: Item de venda não encontrado
    """
    i = controller.obter_item(id)
    return jsonify(i.__dict__) if i else ('', 404)

@bp_itens_venda.route('/', methods=['POST'])
def criar():
    """
    Cria um novo item de venda
    ---
    tags:
      - Itens de Venda
    requestBody:
      required: true
      content:
        application/json:
          example:
            {
              "venda_id": 3,
              "produto_id": 5,
              "quantidade": 2,
              "preco_unitario": 50.0
            }
    responses:
      201:
        description: Item de venda criado com sucesso
        examples:
          application/json:
            {
              "id": 7,
              "venda_id": 3,
              "produto_id": 5,
              "quantidade": 2,
              "preco_unitario": 50.0
            }
    """
    i = controller.criar_item(request.json)
    return jsonify(i.__dict__), 201

@bp_itens_venda.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    """
    Atualiza um item de venda existente
    ---
    tags:
      - Itens de Venda
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do item de venda
    requestBody:
      required: true
      content:
        application/json:
          example:
            {
              "quantidade": 3,
              "preco_unitario": 55.0
            }
    responses:
      200:
        description: Item de venda atualizado com sucesso
        examples:
          application/json:
            {
              "id": 1,
              "venda_id": 3,
              "produto_id": 5,
              "quantidade": 3,
              "preco_unitario": 55.0
            }
      404:
        description: Item de venda não encontrado
    """
    i = controller.atualizar_item(id, request.json)
    return jsonify(i.__dict__) if i else ('', 404)

@bp_itens_venda.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    """
    Deleta um item de venda pelo ID
    ---
    tags:
      - Itens de Venda
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do item de venda
    responses:
      200:
        description: Item de venda deletado com sucesso
        examples:
          application/json:
            { "deleted": True }
      404:
        description: Item de venda não encontrado
    """
    i = controller.deletar_item(id)
    return jsonify({ 'deleted': True }) if i else ('', 404)