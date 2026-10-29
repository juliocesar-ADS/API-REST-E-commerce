# API REST E-commerce

API REST de um e-commerce simples desenvolvida em Python com Flask e integrada ao banco de dados MySQL.

O projeto foi criado com o objetivo de praticar os principais conceitos de desenvolvimento de APIs REST, utilizando métodos HTTP, JSON, operações CRUD e integração com banco de dados.

## Tecnologias utilizadas

- Python
- Flask
- MySQL
- MySQL Connector
- API REST
- JSON
- HTTP
- Postman
- Git e GitHub

## Objetivo do projeto

Este projeto faz parte dos meus estudos de desenvolvimento de APIs REST, com foco na criação de operações CRUD e no tratamento de requisições HTTP.

Durante o desenvolvimento, foram praticados conceitos como:

- Rotas e endpoints
- Métodos HTTP
- Requisições e respostas
- JSON
- Parâmetros de rota
- Códigos de status HTTP
- Operações CRUD
- Validação de dados recebidos
- Tratamento de erros
- Integração entre Python e MySQL
- Comandos SQL (SELECT, INSERT, UPDATE e DELETE)
- Conexão com banco de dados
- Testes de API utilizando Postman

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

## Banco de dados

O projeto utiliza o MySQL para armazenar os produtos cadastrados.

O banco de dados possui uma tabela chamada `produtos`, com os seguintes campos:

| Campo | Tipo | Descrição |
|---|---|---|
| id | INT | Identificador único e auto incremento |
| nome | VARCHAR(60) | Nome do produto |
| preco | DECIMAL(10,2) | Preço do produto |
| estoque | INT | Quantidade disponível em estoque |

## Validações implementadas

A API realiza validações durante o cadastro e a atualização de produtos.

As validações incluem:

- Verificação do formato dos dados recebidos em JSON.
- Verificação da presença dos campos obrigatórios: `nome`, `preco` e `estoque`.
- Verificação para garantir que o nome seja um texto preenchido.
- Verificação para garantir que o preço seja numérico, válido e não negativo.
- Verificação para garantir que o estoque seja um número inteiro e não negativo.
- Rejeição de valores booleanos nos campos de preço e estoque.
- Verificação da existência do produto antes de atualizar ou excluir.

Quando os dados não atendem às validações, a API retorna o status HTTP `400 Bad Request`.

Produtos cadastrados com sucesso retornam `201 Created`, enquanto produtos não encontrados retornam `404 Not Found`.

## Estrutura de um produto

Cada produto possui os seguintes campos:

```json
{
  "id": 1,
  "nome": "Teclado",
  "preco": 150.00,
  "estoque": 10
}
```

## Estrutura do projeto

```text
API-REST-Ecommerce/
│
├── app.py
├── conexao.py
├── estoque.sql
├── requirements.txt
└── README.md
```

## Como executar o projeto

**1. Clone o repositório**

```bash
git clone URL_DO_REPOSITORIO
```

**2. Entre na pasta do projeto**

```bash
cd API-REST-Ecommerce
```

**3. Instale as dependências**

```bash
pip install -r requirements.txt
```

**4. Configure o banco de dados**

- Inicie o MySQL.
- Execute o arquivo `estoque.sql` no MySQL Workbench ou em outro cliente MySQL.
- Confira as configurações de conexão no arquivo `conexao.py`.

**5. Execute a API**

```bash
python app.py
```

Após iniciar, a API estará disponível localmente em:

```text
http://127.0.0.1:5000
```

## Testes

As requisições foram realizadas utilizando o Postman, permitindo testar as operações CRUD, os dados enviados em JSON e as respostas HTTP da API.

## Considerações finais

O desenvolvimento deste projeto proporcionou a prática de conceitos importantes de desenvolvimento backend, desde a criação de rotas e validações até a integração de uma API REST com um banco de dados MySQL.

O projeto também contribuiu para o aprendizado sobre organização de código, tratamento de erros e testes de requisições HTTP.