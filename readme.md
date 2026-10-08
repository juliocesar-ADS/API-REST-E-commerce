# 🛒 API REST E-commerce

API REST de um e-commerce simples desenvolvida em Python com Flask.
O projeto foi criado com o objetivo de praticar os principais conceitos de desenvolvimento de APIs REST, utilizando HTTP, JSON e o Postman para realizar e testar requisições.

## 🚀 Tecnologias utilizadas

* Python
* Flask
* API REST
* JSON
* HTTP
* Postman

## 📚 Objetivo do projeto

Este projeto foi desenvolvido como parte dos meus estudos de desenvolvimento de APIs REST.

Durante o desenvolvimento, foram praticados conceitos como:

* Rotas e endpoints
* Métodos HTTP
* Requisições e respostas
* JSON
* Parâmetros de rota
* Status HTTP
* CRUD
* Manipulação de dados com Python
* Testes de API utilizando Postman

## 🔧 Funcionalidades

A API possui operações para gerenciamento de produtos:

| Método | Endpoint         | Descrição                          |
| ------ | ---------------- | ---------------------------------- |
| GET    | `/`              | Verifica se a API está funcionando |
| GET    | `/produtos`      | Lista todos os produtos            |
| GET    | `/produtos/<id>` | Busca um produto pelo ID           |
| POST   | `/produtos`      | Cria um novo produto               |
| PUT    | `/produtos/<id>` | Atualiza um produto                |
| DELETE | `/produtos/<id>` | Remove um produto                  |

## 📦 Estrutura de um produto

Os produtos possuem os seguintes dados:

```json
{
    "id": 1,
    "nome": "Teclado",
    "preco": 150.00,
    "estoque": 10
}
```

## 🧪 Testando com Postman

A API pode ser testada utilizando o Postman.

### Listar produtos

```http
GET /produtos
```

### Buscar produto

```http
GET /produtos/1
```

### Criar produto

```http
POST /produtos
```

Body:

```json
{
    "nome": "Webcam",
    "preco": 250,
    "estoque": 8
}
```

A API retorna o produto criado com status `201 Created`.

### Atualizar produto

```http
PUT /produtos/1
```

Body:

```json
{
    "nome": "Teclado Mecânico",
    "preco": 200,
    "estoque": 8
}
```

### Excluir produto

```http
DELETE /produtos/1
```

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd nome-do-projeto
```

### 3. Instale o Flask

```bash
pip install flask
```

### 4. Execute a aplicação

```bash
python app.py
```

A API ficará disponível localmente em:

```text
http://127.0.0.1:5000
```

Depois, utilize o Postman para realizar as requisições.

## ⚠️ Observação

Atualmente, os produtos são armazenados em uma lista Python em memória. Isso significa que os dados são perdidos quando a aplicação é reiniciada.

O projeto poderá evoluir posteriormente para utilizar um banco de dados, permitindo a persistência dos produtos.

## 📌 Próximos passos

* [ ] Adicionar banco de dados
* [ ] Criar validações para os dados recebidos
* [ ] Melhorar tratamento de erros
* [ ] Organizar a aplicação em diferentes arquivos
* [ ] Criar testes para os endpoints
* [ ] Documentar melhor a API

## 👨‍💻 Sobre o projeto

Projeto desenvolvido para praticar Python, Flask e desenvolvimento de APIs REST, com foco em aprendizado e construção de portfólio.
