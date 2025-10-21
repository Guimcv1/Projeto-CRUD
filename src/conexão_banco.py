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

