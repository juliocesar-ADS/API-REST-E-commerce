#  API REST E-commerce

API REST de um e-commerce simples desenvolvida em Python com Flask.

O projeto foi criado com o objetivo de praticar os principais conceitos de desenvolvimento de APIs REST, utilizando HTTP, JSON e Postman para realizar e testar requisições.

##  Tecnologias utilizadas

- Python
- Flask
- API REST
- JSON
- HTTP
- Postman
- Git e GitHub

##  Objetivo do projeto

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
- Testes de API com Postman

##  Funcionalidades

A API possui as seguintes operações para gerenciamento de produtos:

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Verifica se a API está funcionando |
| GET | `/produtos` | Lista todos os produtos |
| GET | `/produtos/<id>` | Busca um produto pelo ID |
| POST | `/produtos` | Cadastra um novo produto |
| PUT | `/produtos/<id>` | Atualiza um produto |
| DELETE | `/produtos/<id>` | Remove um produto |

##  Validações implementadas

No cadastro de produtos (`POST /produtos`), a API verifica:

- Se os dados recebidos estão em formato JSON válido.
- Se os campos `nome`, `preco` e `estoque` foram enviados.
- Se o nome é um texto preenchido.

Quando os dados não atendem às validações implementadas, a API retorna o status HTTP `400 Bad Request`.

Produtos cadastrados com sucesso retornam `201 Created`.

**Observação:** a validação do tipo e do valor do preço e do estoque ainda será implementada.

##  Estrutura de um produto

Cada produto possui os seguintes campos:

```json
{
  "id": 1,
  "nome": "Teclado",
  "preco": 150.00,
  "estoque": 10
}
```

- `id`: identificador do produto.
- `nome`: nome do produto.
- `preco`: preço do produto.
- `estoque`: quantidade disponível em estoque.

##  Testando com Postman

A API pode ser testada utilizando o Postman, enviando requisições para o endereço local da aplicação.

### Listar produtos

```http
GET http://127.0.0.1:5000/produtos
```

### Buscar produto

```http
GET http://127.0.0.1:5000/produtos/1
```

### Criar produto

```http
POST http://127.0.0.1:5000/produtos
```

No Postman, selecione **Body → raw → JSON** e envie:

```json
{
  "nome": "Webcam",
  "preco": 250,
  "estoque": 8
}
```

### Exemplo de cadastro inválido

Envie o seguinte JSON para testar a validação do nome:

```json
{
  "nome": "",
  "preco": 150,
  "estoque": 10
}
```

O resultado esperado é o status `400 Bad Request`, com a mensagem de que o nome é obrigatório.

### Atualizar produto

```http
PUT http://127.0.0.1:5000/produtos/1
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
DELETE http://127.0.0.1:5000/produtos/1
```

##  Como executar

### 1. Clone o repositório

Substitua `URL_DO_REPOSITORIO` pelo endereço real do seu repositório no GitHub.

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

##  Limitações atuais

Atualmente, os produtos são armazenados em uma lista Python em memória. Isso significa que os dados são perdidos quando a aplicação é reiniciada.

Além disso, a validação do cadastro ainda não verifica se o preço e o estoque possuem tipos e valores adequados. O endpoint de atualização também poderá receber validações mais completas em etapas futuras.

## Próximos passos

- [x] Implementar operações CRUD de produtos
- [x] Validar o formato JSON recebido no cadastro
- [x] Verificar a presença dos campos obrigatórios
- [x] Validar o nome do produto
- [ ] Validar o tipo e os valores do preço e do estoque
- [ ] Melhorar as validações na atualização de produtos
- [ ] Melhorar o tratamento de erros
- [ ] Adicionar banco de dados
- [ ] Organizar a aplicação em diferentes arquivos
- [ ] Criar testes automatizados
- [ ] Melhorar a documentação da API

## Sobre o projeto

Projeto desenvolvido para praticar Python, Flask e desenvolvimento de APIs REST, com foco no aprendizado contínuo e na construção de um portfólio para a área de desenvolvimento de software.