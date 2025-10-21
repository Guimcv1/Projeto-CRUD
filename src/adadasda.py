import mysql.connector

# Configurações da conexão
config = {
    'user': 'usuario',
    'password': 'senha',
    'host': 'localhost',
    'database': 'nome_banco'
}
# Conectando ao banco
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

def criar_usuario(nome, email):
    sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
    valores = (nome, email)
    cursor.execute(sql, valores)
    conn.commit()
    print(f"Usuário {nome} inserido com sucesso!")

def ler_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    resultado = cursor.fetchall()
    for linha in resultado:
        print(linha)

if __name__ == "__main__":
    while True:
        nome = input("Digite o nome do usuário (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        email = input("Digite o email do usuário: ")
        criar_usuario(nome, email)

    print("\nLista completa de usuários:")
    ler_usuarios()

# Fechando conexão
cursor.close()
conn.close()
