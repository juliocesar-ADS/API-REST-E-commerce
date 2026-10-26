from flask import Flask, jsonify, request

produtos = []

app = Flask(__name__)

#rota principal da api
@app.route("/", methods=["GET"])
def mensagem():
    return jsonify({
        "Status": "API E-commerce funcionando!",
        "Rotas": "/produtos    /produtos/id",
        "Modos": "GET, POST, PUT e DELETE."
    })

#mostrar todos produtos criados
@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

#criar um produto
@app.route("/produtos", methods=["POST"])
def criar_produtos():
    dados = request.get_json()

    if not isinstance(dados, dict):
        return jsonify({"mensagem": "Envie um JSON válido."}), 400

    if not all(campo in dados for campo in ["nome", "preco", "estoque"]):
        return jsonify({"mensagem": "Cadastre todos os campos."}), 400

    if not isinstance(dados["nome"], str) or dados["nome"].strip() == "":
        return jsonify({"mensagem": "O nome é obrigatório."}), 400

    if isinstance(dados["preco"], bool) or not isinstance(dados["preco"], (int, float)):
        return jsonify({"mensagem": "O Preço deve ser um número."}), 400

    if dados["preco"] < 0:
        return jsonify({"mensagem": "O preço não pode ser negativo."}), 400

    if isinstance(dados["estoque"], bool) or not isinstance(dados["estoque"], int):
        return jsonify({"mensagem": "O estoque deve ser um número inteiro."}), 400

    if dados["estoque"] < 0:
        return jsonify({"mensagem": "O estoque não pode ser negativo."}), 400

    ids = []

    for produto in produtos:
        ids.append(produto["id"])

    if not ids:
        novo_id = 1
    else:
        novo_id = max(ids) + 1

    novo_produto = {
        "id": novo_id,
        "nome": dados["nome"],
        "preco": dados["preco"],
        "estoque": dados["estoque"]}

    produtos.append(novo_produto)

    return jsonify(novo_produto), 201

#listar produto especifico
@app.route("/produtos/<int:id>", methods=["GET"])
def buscar_produtos(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify (produto)
    return jsonify({"erro": "produto não encontrado"}), 404

#atualizar produtos
@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    dados = request.get_json()

    if not isinstance(dados, dict):
        return jsonify({"mensagem": "Envie um JSON válido."}), 400

    if not all(campo in dados for campo in ["nome", "preco", "estoque"]):
        return jsonify({"mensagem": "Cadastre todos os campos."}), 400

    if not isinstance(dados["nome"], str) or dados["nome"].strip() == "":
        return jsonify({"mensagem": "O nome é obrigatório."}), 400

    if isinstance(dados["preco"], bool) or not isinstance(dados["preco"], (int, float)):
        return jsonify({"mensagem": "O preço deve ser um número."}), 400

    if dados["preco"] < 0:
        return jsonify({"mensagem": "O preço não poder ser negativo."}), 400

    if isinstance(dados["estoque"], bool) or not isinstance(dados["estoque"], int):
        return jsonify({"mensagem": "O estoque deve ser um número inteiro."}), 400

    if dados["estoque"] < 0:
        return jsonify({"mensagem": "O estoque não poder ser negativo."}), 400

    for produto in produtos:
        if produto["id"] == id:
            produto["nome"] = dados["nome"]
            produto["preco"] = dados["preco"]
            produto["estoque"] = dados["estoque"]

            return jsonify(produto)
    return jsonify({"erro": "produto não encontrado"}), 404


#deletar produtos
@app.route("/produtos/<int:id>", methods=["DELETE"])
def excluir_produto(id):

    for produto in produtos:
        if produto["id"] == id:
            produtos.remove(produto)
            return jsonify({
                "produto": produto,
                "mensagem": "Produto removido."})
    return jsonify({"erro": "produto não encontrado."}), 404


if __name__ == "__main__":
    app.run(debug=True)