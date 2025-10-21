from conexão_banco import conn
from conexão_banco import cursor
import time
from passlib.hash import django_bcrypt_sha256 as sha256

while True:
    def login():
        while True:
            print(20*"-","Bem vindo ao banco de dados",20*"-")
            user = input("Digite o nome do usuario: ")
            senha = input("Digite a senha: ")
            # tem que pegar os dados e comparar com o banco

            var = sha256.hash(input)

            sha256.verify(input,hash)

            if user == user_banco and senha == senha_banco:
                interface()
            else:
                print("Nome de usuario ou senhas incorretas")
                time.sleep(2)
                continue


    def interface():
        print("1 | Criar Tabela")
        print("2 | Cadastrar Produto")
        print("3 | Listar Produto")
        print("4 | Editar Produto")
        print("5 | Vender produto")
        print("6 | Sair")
        op = int(input(""))
        match op:
            case 1:
                print("1 | Criar tabela de usuario")
                print("2 | Criar tabela de produto")
                i = int(input(''))
                match i:
                    case 1:
                        criar_tabela_pes()
                    case 2:
                        criar_tabela_prod()
            case 2:
                cadastro_p()
            case 3:
                listar()
            case 4:
                editar()
            case 5:
                vender()
            case 6:
                break

    def criar_tabela_prod():
        try:
              cursor.execute('''
              CREATE TABLE TB_Produtos(
                ID INTEGER PRIMARY KEY,
                nome VARCHAR(120) NOT NULL,
                quantidade VARCHAR(120) NOT NULL,
                validade VARCHAR(120),
                preco VARCHAR(120) NOT NULL
              );
        ''')
        except Exception as e:
                print(f'Falha ap criar uma tabela: {e}')

    def criar_tabela_pes():
        try:
              cursor.execute('''
              CREATE TABLE TB_Produtos(
                ID INTEGER PRIMARY KEY,
                email VARCHAR(120) NOT NULL,
                senha VARCHAR(120) NOT NULL,

              );
        ''')
        except Exception as e:
                print(f'Falha ap criar uma tabela: {e}')

    def cadastro_p():
        nome = input("Digite o nome do produto: ")
        validade = input("Digite a data de validade do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        valor = float(input("Digite o preço: R$"))
        sql = "INSERT INTO TB_Produtos (nome, validade, quantidade, valor) VALUES (%s, %s, %s, %s)"
        valores = (nome, validade, quantidade, valor)
        cursor.execute(sql, valores)
        conn.commit()
        print(f"Produto {nome} cadastrado com sucesso!")

    def listar():
        cursor.execute("SELECT * FROM TB_Produtos")
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha)

    def editar():
        produto = input("ID do Produto a ser editado: ")
        print("O que deseja editar?")
        print("1 | Editar o nome")
        print("2 | Editar o Valor")
        print("3 | Editar a validade")
        print("4 | Editar a quantidade")
        op = int(input(""))
        match op:
            case 1:
                nome = input("Digite o novo nome: ")
                sql = "UPDATE TB_Produtos SET nome = (%s) WHERE (%s)"
                cursor.execute(sql, nome, produto)
            case 2:
                valor = input("Digite o novo valor: ")
                sql = "UPDATE TB_Produtos SET valor = (%s) WHERE (%s)"
                cursor.execute(sql, valor, produto)
            case 3:
                validade = input("Digite a Validade: ")
                sql = "UPDATE TB_Produtos SET validade = (%s) WHERE (%s)"
                cursor.execute(sql, validade, produto)
            case 4:
                quantidade = input("Digite a quantidade: ")
                sql = "UPDATE TB_Produtos SET quantidade = (%s) WHERE (%s)"
                cursor.execute(sql, quantidade, produto)

    def vender():
        op = int(input('ID do produto a ser vendido: '))
        quantidade = input("Digite a quantidade: ")
        sql = "UPDATE TB_Produtos SET quantidade = (%s) WHERE (%s)"
        cursor.execute(sql, quantidade, produto)
        print(f"Quantidade de Produto: {num_p}")
        num = int(input("Digite a quantidade de Produto: "))
        if num < num_p:
            print("Quantidade de produto insuficiente")
            print(f"Tente com outro valor menor que {num_p + 1}")

    login()