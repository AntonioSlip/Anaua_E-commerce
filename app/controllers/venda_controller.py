from flask import jsonify, request
from app.services import Venda_service

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
    vendas = Venda_service.listar_vendas()
    return jsonify([v.to_dict() for v in vendas])

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
    v = Venda_service.obter_venda(id)
    return jsonify(v.to_dict()) if v else ('', 404)

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
    v = Venda_service.criar_venda(request.json)
    return jsonify(v.to_dict()), 201

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
    v = Venda_service.atualizar_venda(id, request.json)
    return jsonify(v.to_dict()) if v else ('', 404)

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
    v = Venda_service.deletar_venda(id)
    return jsonify({ 'deleted': True }) if v else ('', 404)
