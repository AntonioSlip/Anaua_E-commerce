from flask import jsonify, request
from app.services import ItemVenda_service

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
    itens = ItemVenda_service.listar_itens()
    return jsonify([i.to_dict() for i in itens])

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
    i = ItemVenda_service.obter_item(id)
    return jsonify(i.to_dict()) if i else ('', 404)

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
    i = ItemVenda_service.criar_item(request.json)
    return jsonify(i.to_dict()), 201

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
    i = ItemVenda_service.atualizar_item(id, request.json)
    return jsonify(i.to_dict()) if i else ('', 404)

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
    i = ItemVenda_service.deletar_item(id)
    return jsonify({ 'deleted': True }) if i else ('', 404)
