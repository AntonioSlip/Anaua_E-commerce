from flask import jsonify, request
from app.services import Categoria_service

def listar_categorias():
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
    categorias = Categoria_service.listar_categorias()
    return jsonify([c.to_dict() for c in categorias]), 200

def obter_categoria(id):
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
    categoria = Categoria_service.obter_categoria(id)
    if not categoria:
        return '', 404
    return jsonify(categoria.to_dict()), 200

def criar_categoria():
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
    data = request.json
    nova = Categoria_service.criar_categoria(data)
    return jsonify(nova.to_dict()), 201

def atualizar_categoria(id):
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
    data = request.json
    atualizada = Categoria_service.atualizar_categoria(id, data)
    if not atualizada:
        return '', 404
    return jsonify(atualizada.to_dict()), 200

def deletar_categoria(id):
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
    apagada = Categoria_service.deletar_categoria(id)
    if not apagada:
        return '', 404
    return jsonify({ "deleted": True }), 200
