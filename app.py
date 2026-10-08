from flask import Flask, jsonify, request

produtos = [
    {"id": 1, "nome": "Teclado", "preco": 150.00, "estoque": 10},
    {"id": 2, "nome": "Mouse", "preco": 80.00, "estoque": 20},
    {"id": 3, "nome": "Monitor", "preco": 1200.00, "estoque": 5},
    {"id": 4, "nome": "Cadeira Gamer", "preco": 800.00, "estoque": 3},
    {"id": 5, "nome": "Headset", "preco": 200.00, "estoque": 15}]

app = Flask(__name__)

#rota principal da api
@app.route("/", methods=["GET"])
def mensagem():
    return jsonify({
        "mensagem": "API E-commerce funcionando!",
        "Rotas": "/produtos    /produtos/id",
        "modos": "GET, POST, PUT e DELETE."
    })

#mostrar todos produtos criados
@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

#criar um produto
@app.route("/produtos", methods=["POST"])
def criar_produtos():
    dados = request.get_json()

    ids = []

    for produto in produtos:
        ids.append(produto["id"])
    
    
    novo_id = max(ids) + 1

    print(ids)
    print(novo_id)

    novo_produto = {
        "id": novo_id,
        "nome": dados["nome"],
        "preco": dados["preco"],
        "estoque": dados["estoque"],
    }

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