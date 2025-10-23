import mysql.connector

# Configurações da conexão
config = {
    'user': '3c571c1b794a48358fc2258c2b5ade29',
    'password': 'Gm7856cv12',
    'port':'3306',
    'host': 'mysql.shardatabases.app',
    'database': 'database'
}
# Conectando ao banco
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

