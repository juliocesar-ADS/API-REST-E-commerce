# API REST E-commerce

API REST de um e-commerce simples desenvolvida em Python com Flask.

O projeto foi criado com o objetivo de praticar os principais conceitos de desenvolvimento de APIs REST, utilizando HTTP, JSON e Postman para realizar e testar requisições.

## Tecnologias utilizadas

- Python
- Flask
- API REST
- JSON
- HTTP
- Postman
- Git e GitHub

## Objetivo do projeto

Este projeto faz parte dos meus estudos de desenvolvimento de APIs REST, com foco na criação de operações CRUD e no tratamento das requisições HTTP.

Durante o desenvolvimento, são praticados conceitos como:

- Rotas e endpoints
- Métodos HTTP
- Requisições e respostas
- JSON
- Parâmetros de rota
- Códigos de status HTTP
- CRUD
- Manipulação de listas e dicionários em Python
- Validação de dados recebidos
- Tratamento de erros
- Testes de API com Postman

## Funcionalidades

A API possui as seguintes operações para gerenciamento de produtos:

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Verifica se a API está funcionando |
| GET | `/produtos` | Lista todos os produtos |
| GET | `/produtos/<id>` | Busca um produto pelo ID |
| POST | `/produtos` | Cadastra um novo produto |
| PUT | `/produtos/<id>` | Atualiza um produto |
| DELETE | `/produtos/<id>` | Remove um produto |

## Validações implementadas

A API realiza validações durante o cadastro e a atualização de produtos.

As validações incluem:

- Verificação do formato dos dados recebidos em JSON.
- Verificação da presença dos campos obrigatórios: `nome`, `preco` e `estoque`.
- Verificação para garantir que o nome seja um texto preenchido.
- Verificação para garantir que o preço seja numérico e não negativo.
- Verificação para garantir que o estoque seja um número inteiro e não negativo.
- Rejeição de valores booleanos nos campos de preço e estoque.

Quando os dados não atendem às validações, a API retorna o status HTTP `400 Bad Request`.

Produtos cadastrados com sucesso retornam `201 Created`.

As validações foram testadas utilizando o Postman, incluindo casos com dados inválidos.

## Estrutura de um produto

Cada produto possui os seguintes campos:

```json
{
  "id": 1,
  "nome": "Teclado",
  "preco": 150.00,
  "estoque": 10
}