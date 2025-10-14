# Fazer a conecção com o my SQL usando bibliotecas externas
# Para criar um ambiente virtual usando o: python -m venv 

#importar as bibliotecas de conecção
import mysql
import mysql.connector as mysql
from mysql.connector import Error
from os import getenv
from dotenv import load_dotenv

load_dotenv()

print("O codigo iniciou")

try:
    #objeto de conexão
    conn = mysql.connect(
    host=getenv("host"),
    user=getenv("user"),
    password=getenv("passoword"),
    port=3306,
    database=getenv("database")
    )

    if conn.is_connected():
        print("ok")
    else:
        print("erro")
        
except mysql.Error as e:
    print(e)