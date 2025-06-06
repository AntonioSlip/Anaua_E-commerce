from flask import Blueprint, jsonify, request
from app.controllers import venda_controller as controller

bp_vendas = Blueprint('vendas', __name__, url_prefix='/vendas')

@bp_vendas.route('/', methods=['GET'])
def listar():
    """
    Lista todas as vendas
    ---
    tags:
      - Vendas
    responses:
      200:
        description: Lista de vendas
        examples:
          application/json: [
            {
              "id": 1,
              "usuario_id": 2,
              "data": "2024-06-01T14:35:22",
              "valor_total": 250.75,
              "forma_pagamento": "Cartão de Crédito"
            }
          ]
    """
    vendas = controller.listar_vendas()
    return jsonify([v.__dict__ for v in vendas])

@bp_vendas.route('/<int:id>', methods=['GET'])
def obter(id):
    """
    Retorna uma venda específica pelo ID
    ---
    tags:
      - Vendas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da venda
    responses:
      200:
        description: Venda encontrada
        examples:
          application/json:
            {
              "id": 1,
              "usuario_id": 2,
              "data": "2024-06-01T14:35:22",
              "valor_total": 250.75,
              "forma_pagamento": "Cartão de Crédito"
            }
      404:
        description: Venda não encontrada
    """
    v = controller.obter_venda(id)
    return jsonify(v.__dict__) if v else ('', 404)

@bp_vendas.route('/', methods=['POST'])
def criar():
    """
    Cria uma nova venda
    ---
    tags:
      - Vendas
    requestBody:
      required: true
      content:
        application/json:
          example:
            {
              "usuario_id": 2,
              "valor_total": 250.75,
              "forma_pagamento": "Cartão de Crédito"
            }
    responses:
      201:
        description: Venda criada com sucesso
        examples:
          application/json:
            {
              "id": 3,
              "usuario_id": 2,
              "data": "2024-06-01T14:35:22",
              "valor_total": 250.75,
              "forma_pagamento": "Cartão de Crédito"
            }
    """
    v = controller.criar_venda(request.json)
    return jsonify(v.__dict__), 201

@bp_vendas.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    """
    Atualiza uma venda existente
    ---
    tags:
      - Vendas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da venda
    requestBody:
      required: true
      content:
        application/json:
          example:
            {
              "usuario_id": 2,
              "valor_total": 280.00,
              "forma_pagamento": "Pix"
            }
    responses:
      200:
        description: Venda atualizada com sucesso
        examples:
          application/json:
            {
              "id": 1,
              "usuario_id": 2,
              "valor_total": 280.00,
              "forma_pagamento": "Pix"
            }
      404:
        description: Venda não encontrada
    """
    v = controller.atualizar_venda(id, request.json)
    return jsonify(v.__dict__) if v else ('', 404)

@bp_vendas.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    """
    Deleta uma venda pelo ID
    ---
    tags:
      - Vendas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da venda
    responses:
      200:
        description: Venda deletada com sucesso
        examples:
          application/json:
            { "deleted": true }
      404:
        description: Venda não encontrada
    """
    v = controller.deletar_venda(id)
    return jsonify({ 'deleted': True }) if v else ('', 404)