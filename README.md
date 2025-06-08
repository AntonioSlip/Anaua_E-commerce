
# Anauá E-commerce

Este é um projeto web desenvolvido com [Flask](https://flask.palletsprojects.com/) que serve como base para um sistema de e-commerce.

## 🚀 Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/) — Framework web leve e flexível em Python
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) — ORM para integração com bancos de dados
- [Flasgger](https://github.com/flasgger/flasgger) — Geração de documentação Swagger para APIs
- [OpenCV](https://opencv.org/) e [NumPy](https://numpy.org/) — Para processamento e manipulação de imagens (quando aplicável)
- [Jinja2](https://jinja.palletsprojects.com/) — Engine de templates usada pelo Flask

## 📦 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/anaua_ecommerce.git
   cd anaua_ecommerce
   ```

2. Crie um ambiente virtual (recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Executando o Projeto

Para iniciar o servidor Flask em modo de desenvolvimento:

```bash
python run.py
```

A aplicação será iniciada em `http://127.0.0.1:5000/`.

## 📁 Estrutura Básica

```
anaua_ecommerce/
├── app/                # Pacote principal da aplicação Flask
├── run.py              # Arquivo principal para rodar o servidor
├── requirements.txt    # Dependências da aplicação
└── .gitignore          # Arquivos ignorados pelo Git
```

## 📝 Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT). Sinta-se livre para usá-lo, modificá-lo e distribuí-lo.

## 📌 Endpoints da API

#### `/produto`
| Método | Rota                | Descrição                   |
|--------|---------------------|-----------------------------|
| GET    | `/`                 | Lista todos os produtos     |
| GET    | `/<int:produto_id>` | Busca um produto específico |
| POST   | `/`                 | Cria um novo produto        |
| PUT    | `/<int:produto_id>` | Atualiza um produto         |
| DELETE | `/<int:produto_id>` | Remove um produto           |

#### `/usuario`
| Método | Rota          | Descrição                     |
|--------|---------------|-------------------------------|
| GET    | `/`           | Lista todos os usuários       |
| GET    | `/<int:id>`   | Busca um usuário específico   |
| POST   | `/`           | Cria um novo usuário          |
| PUT    | `/<int:id>`   | Atualiza dados do usuário     |
| DELETE | `/<int:id>`   | Remove um usuário             |

#### `/venda`
| Método | Rota          | Descrição                   |
|--------|---------------|-----------------------------|
| GET    | `/`           | Lista todas as vendas       |
| GET    | `/<int:id>`   | Busca uma venda específica  |
| POST   | `/`           | Cria uma nova venda         |
| PUT    | `/<int:id>`   | Atualiza uma venda          |
| DELETE | `/<int:id>`   | Remove uma venda            |

#### `/categoria`
| Método | Rota            | Descrição                      |
|--------|-----------------|--------------------------------|
| GET    | `/`             | Lista todas as categorias      |
| GET    | `/<int:id>`     | Busca uma categoria específica |
| POST   | `/`             | Cria uma nova categoria        |
| PUT    | `/<int:id>`     | Atualiza uma categoria         |
| DELETE | `/<int:id>`     | Remove uma categoria           |

#### `/itens-venda`
| Método | Rota            | Descrição                           |
|--------|-----------------|-------------------------------------|
| GET    | `/`             | Lista todos os itens de venda       |
| GET    | `/<int:id>`     | Retorna um item de venda específico |
| POST   | `/`             | Cria um novo item de venda          |
| PUT    | `/<int:id>`     |Atualiza um item de venda existente  |
| DELETE | `/<int:id>`     | Remove um item de venda             |
