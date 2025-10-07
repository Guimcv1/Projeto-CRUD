# Fazer a conecção com o my SQL usando bibliotecas externas
# Para criar um ambiente virtual usando o: python -m venv 

#importar as bibliotecas de conecção
import mysql.connector

# Conectar ao server
db = mysql.connector.connect(
    host="mysql.shardatabases.app",
    port=3306,
    user="4a17d1e1fbce429a854799ccb20d674c",
    password="testeteste")

# Pegar o controle
cur = db.cursor()

# Execute a query
cur.execute("SELECT CURDATE()")

# Pegar um resultado
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

# Encerar a conecção 
db.close()