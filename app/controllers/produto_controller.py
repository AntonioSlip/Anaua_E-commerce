from flask import jsonify, request
from app.services import Produto_service

def get_all():
    """
    Lista todos os produtos
    ---
    tags:
      - Produtos
    responses:
      200:
        description: Lista de produtos
        examples:
          application/json: [
            {
              "id": 1,
              "nome": "Produto Exemplo",
              "preco": 100.0,
              "estoque": 10,
              "categoria_id": 1
            }
          ]
    """
    produtos = Produto_service.listar_produtos()
    return jsonify([{
        'id': p.id,
        'nome': p.nome,
        'descricao': p.descricao,
        'preco': p.preco,
        'estoque': p.estoque,
        'foto_url': p.foto_url,
        'categoria_id': p.categoria_id
    } for p in produtos])

def get_one(produto_id):
    """
    Retorna um produto específico pelo ID
    ---
    tags:
      - Produtos
    parameters:
      - name: produto_id
        in: path
        type: integer
        required: true
        description: ID do produto
    responses:
      200:
        description: Produto encontrado
        examples:
          application/json:
            {
              "id": 1,
              "nome": "Produto Exemplo",
              "descricao": "Descrição",
              "preco": 100.0,
              "estoque": 10,
              "foto_url": "http://...",
              "categoria_id": 1
            }
      404:
        description: Produto não encontrado
    """
    produto = Produto_service.obter_produto(produto_id)
    if produto:
        return jsonify({
            'id': produto.id,
            'nome': produto.nome,
            'descricao': produto.descricao,
            'preco': produto.preco,
            'estoque': produto.estoque,
            'foto_url': produto.foto_url,
            'categoria_id': produto.categoria_id
        })
    return jsonify({'erro': 'Produto não encontrado'}), 404

def create():
    """
    Cria um novo produto
    ---
    tags:
      - Produtos
    requestBody:
      required: true
      content:
        application/json:
          example:
            {
              "nome": "Novo Produto",
              "descricao": "Descrição",
              "preco": 150.0,
              "estoque": 5,
              "foto_url": "http://...",
              "categoria_id": 1
            }
    responses:
      201:
        description: Produto criado com sucesso
        examples:
          application/json:
            { "id": 2 }
    """
    data = request.json
    produto = Produto_service.criar_produto(data)
    return jsonify({'id': produto.id}), 201

def update(produto_id):
    """
    Atualiza um produto existente
    ---
    tags:
      - Produtos
    parameters:
      - name: produto_id
        in: path
        type: integer
        required: true
        description: ID do produto a ser atualizado
    requestBody:
      required: true
      content:
        application/json:
          example:
            {
              "nome": "Produto Atualizado",
              "descricao": "Nova descrição",
              "preco": 200.0,
              "estoque": 7,
              "foto_url": "http://...",
              "categoria_id": 1
            }
    responses:
      200:
        description: Produto atualizado com sucesso
        examples:
          application/json:
            { "mensagem": "Produto atualizado" }
      404:
        description: Produto não encontrado
    """
    data = request.json
    produto = Produto_service.atualizar_produto(produto_id, data)
    if produto:
        return jsonify({'mensagem': 'Produto atualizado'})
    return jsonify({'erro': 'Produto não encontrado'}), 404

def delete(produto_id):
    """
    Deleta um produto pelo ID
    ---
    tags:
      - Produtos
    parameters:
      - name: produto_id
        in: path
        type: integer
        required: true
        description: ID do produto
    responses:
      200:
        description: Produto deletado com sucesso
        examples:
          application/json:
            { "mensagem": "Produto deletado" }
      404:
        description: Produto não encontrado
    """
    produto = Produto_service.deletar_produto(produto_id)
    if produto:
        return jsonify({'mensagem': 'Produto deletado'})
    return jsonify({'erro': 'Produto não encontrado'}), 404
