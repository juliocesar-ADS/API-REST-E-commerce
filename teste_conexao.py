from conexao import conectar

conexao = None

try:
    conexao = conectar()

    if conexao.is_connected():
        print("Conexão com o MsSQL realizada com sucesso!")

except Exception as erro:
    print("Erro ao conectar com o mySQL:", erro)

finally:
    if conexao is not None and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada.")