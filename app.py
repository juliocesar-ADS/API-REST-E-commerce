
from flask import Flask, jsonify, request
from conexao import conectar
from math import isfinite
from decimal import Decimal

app = Flask(__name__)


# Converte valores Decimal do MySQL para float,
# permitindo que sejam enviados como JSON.
def preparar_produto(produto):
    if produto is None:
        return None

    produto["preco"] = float(produto["preco"])
    return produto


# Valida os dados recebidos no POST e PUT.
def validar_dados(dados):
    if not isinstance(dados, dict):
        return "Envie um JSON válido."

    campos = ["nome", "preco", "estoque"]

    if not all(campo in dados for campo in campos):
        return "Informe todos os campos: nome, preco e estoque."

    if not isinstance(dados["nome"], str) or not dados["nome"].strip():
        return "O nome é obrigatório e deve ser um texto."

    preco = dados["preco"]

    if (
        isinstance(preco, bool)
        or not isinstance(preco, (int, float, Decimal))
        or not isfinite(float(preco))
        or preco < 0
    ):
        return "O preço deve ser um número válido e não negativo."

    estoque = dados["estoque"]

    if (
        isinstance(estoque, bool)
        or not isinstance(estoque, int)
        or estoque < 0
    ):
        return "O estoque deve ser um número inteiro não negativo."

    return None


# Rota principal da API
@app.route("/", methods=["GET"])
def mensagem():
    return jsonify({
        "status": "API E-commerce funcionando!",
        "rotas": {
            "listar_produtos": "GET /produtos",
            "cadastrar_produto": "POST /produtos",
            "buscar_produto": "GET /produtos/<id>",
            "atualizar_produto": "PUT /produtos/<id>",
            "excluir_produto": "DELETE /produtos/<id>"
        }
    }), 200


# Listar todos os produtos
@app.route("/produtos", methods=["GET"])
def listar_produtos():
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        produtos = [preparar_produto(p) for p in produtos]

        return jsonify(produtos), 200

    except Exception as erro:
        print("Erro ao listar produtos:", erro)

        return jsonify({
            "erro": "Não foi possível listar os produtos."
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()


# Cadastrar um produto
@app.route("/produtos", methods=["POST"])
def criar_produto():
    dados = request.get_json(silent=True)

    erro_validacao = validar_dados(dados)

    if erro_validacao:
        return jsonify({"erro": erro_validacao}), 400

    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO produtos (nome, preco, estoque)
            VALUES (%s, %s, %s)
        """

        valores = (
            dados["nome"].strip(),
            dados["preco"],
            dados["estoque"]
        )

        cursor.execute(sql, valores)
        conexao.commit()

        novo_produto = {
            "id": cursor.lastrowid,
            "nome": dados["nome"].strip(),
            "preco": float(dados["preco"]),
            "estoque": dados["estoque"]
        }

        return jsonify(novo_produto), 201

    except Exception as erro:
        if conexao is not None and conexao.is_connected():
            conexao.rollback()

        print("Erro ao cadastrar produto:", erro)

        return jsonify({
            "erro": "Não foi possível cadastrar o produto."
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()


# Buscar um produto pelo ID
@app.route("/produtos/<int:id>", methods=["GET"])
def buscar_produto(id):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM produtos WHERE id = %s",
            (id,)
        )

        produto = cursor.fetchone()

        if produto is None:
            return jsonify({
                "erro": "Produto não encontrado."
            }), 404

        return jsonify(preparar_produto(produto)), 200

    except Exception as erro:
        print("Erro ao buscar produto:", erro)

        return jsonify({
            "erro": "Não foi possível buscar o produto."
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()


# Atualizar um produto
@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    dados = request.get_json(silent=True)

    erro_validacao = validar_dados(dados)

    if erro_validacao:
        return jsonify({"erro": erro_validacao}), 400

    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM produtos WHERE id = %s",
            (id,)
        )

        produto = cursor.fetchone()

        if produto is None:
            return jsonify({
                "erro": "Produto não encontrado."
            }), 404

        sql = """
            UPDATE produtos
            SET nome = %s, preco = %s, estoque = %s
            WHERE id = %s
        """

        valores = (
            dados["nome"].strip(),
            dados["preco"],
            dados["estoque"],
            id
        )

        cursor.execute(sql, valores)
        conexao.commit()

        produto_atualizado = {
            "id": id,
            "nome": dados["nome"].strip(),
            "preco": float(dados["preco"]),
            "estoque": dados["estoque"]
        }

        return jsonify(produto_atualizado), 200

    except Exception as erro:
        if conexao is not None and conexao.is_connected():
            conexao.rollback()

        print("Erro ao atualizar produto:", erro)

        return jsonify({
            "erro": "Não foi possível atualizar o produto."
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()


# Excluir um produto
@app.route("/produtos/<int:id>", methods=["DELETE"])
def excluir_produto(id):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM produtos WHERE id = %s",
            (id,)
        )

        produto = cursor.fetchone()

        if produto is None:
            return jsonify({
                "erro": "Produto não encontrado."
            }), 404

        cursor.execute(
            "DELETE FROM produtos WHERE id = %s",
            (id,)
        )

        conexao.commit()

        return jsonify({
            "mensagem": "Produto removido com sucesso.",
            "produto": preparar_produto(produto)
        }), 200

    except Exception as erro:
        if conexao is not None and conexao.is_connected():
            conexao.rollback()

        print("Erro ao excluir produto:", erro)

        return jsonify({
            "erro": "Não foi possível excluir o produto."
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()


if __name__ == "__main__":
    app.run(debug=True)
