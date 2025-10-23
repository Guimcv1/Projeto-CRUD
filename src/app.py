from conexão_banco import conn, cursor
from passlib.hash import pbkdf2_sha256 as sha256
import time
import pwinput


def criar_tabela_prod():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TB_Produtos(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(255) NOT NULL,
                quantidade INTEGER NOT NULL,
                validade REAL,
                preco REAL NOT NULL
            );
        ''')
        conn.commit()
        print("Tabela de produtos criada (ou já existente).")
    except Exception as e:
        print(f"Falha ao criar tabela de produtos: {e}")

def criar_tabela_pes():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TB_Usuarios(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                usuario VARCHAR(120) NOT NULL UNIQUE,
                senha VARCHAR(255) NOT NULL
            );
        ''')
        conn.commit()
        print("Tabela de usuários criada (ou já existente).")
    except Exception as e:
        print(f"Falha ao criar tabela de usuários: {e}")

def cadastrar_usuario():
    usuario = input("Digite o nome do usuário: ")
    senha = pwinput.pwinput(prompt="Digite a senha: ")
    senha_hash = sha256.hash(senha)
    try:
        cursor.execute("INSERT INTO TB_Usuarios (usuario, senha) VALUES (%s, %s)", (usuario, senha_hash))
        conn.commit()
        print(f"Usuário {usuario} cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")

def login():
    while True:
        print("\n" + 20*"-", "Login no sistema", 20*"-")
        user = input("Usuário: ")
        senha = pwinput.pwinput("Senha: ")
        sql = "SELECT senha FROM TB_Usuarios WHERE usuario = %s"
        cursor.execute(sql,(user,))
        result = cursor.fetchone()

        if result and sha256.verify(senha, result[0]):
            print("\nLogin bem-sucedido!")
            interface()
            break
        else:
            print("Usuário ou senha incorretos.")
            time.sleep(2)

def cadastro_produto():
    nome = input("Digite o nome do produto: ")
    validade = input("Digite a validade: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: R$"))
    sql = "INSERT INTO TB_Produtos (nome, validade, quantidade, preco) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nome, validade, quantidade, preco))
    conn.commit()
    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_produtos():
    cursor.execute("SELECT * FROM TB_Produtos")
    produtos = cursor.fetchall()
    if produtos:
        print("\n--- LISTA DE PRODUTOS ---")
        for p in produtos:
            print(f"ID: {p[0]} | Nome: {p[1]} | Quantidade: {p[2]} | Validade: {p[3]} | Preço: R${p[4]:.2f}")
    else:
        print("Nenhum produto cadastrado.")

def editar_produto():
    listar_produtos()
    produto_id = int(input("\nDigite o ID do produto a ser editado: "))

    print("O que deseja editar?")
    print("1 | Nome")
    print("2 | Preço")
    print("3 | Validade")
    print("4 | Quantidade")
    op = int(input("Escolha: "))

    if op == 1:
        novo = input("Novo nome: ")
        campo = "nome"
    elif op == 2:
        novo = float(input("Novo preço: R$"))
        campo = "preco"
    elif op == 3:
        novo = input("Nova validade: ")
        campo = "validade"
    elif op == 4:
        novo = int(input("Nova quantidade: "))
        campo = "quantidade"
    else:
        print("Opção inválida.")
        return

    cursor.execute("UPDATE TB_Produtos SET {campo} = %s WHERE id = %s", (novo, produto_id))
    conn.commit()
    print("Produto atualizado com sucesso!")

def vender_produto():
    listar_produtos()
    produto_id = int(input("\nDigite o ID do produto a ser vendido: "))
    qtd_venda = int(input("Quantidade a vender: "))

    cursor.execute("SELECT quantidade, nome FROM TB_Produtos WHERE id = %s", (produto_id,))
    result = cursor.fetchone()

    if not result:
        print("Produto não encontrado.")
        return

    qtd_atual, nome = result

    if qtd_venda > qtd_atual:
        print(f"Quantidade insuficiente. Estoque atual: {qtd_atual}")
    else:
        nova_qtd = qtd_atual - qtd_venda
        cursor.execute("UPDATE TB_Produtos SET quantidade = %s WHERE id = %s", (nova_qtd, produto_id))
        conn.commit()
        print(f"Venda realizada! {nome} agora tem {nova_qtd} unidades em estoque.")

def deletar_produto():
    listar_produtos()
    produto_id = int(input("\nDigite o ID do produto que deseja deletar: "))

    cursor.execute("SELECT nome FROM TB_Produtos WHERE id = %s", (produto_id,))
    result = cursor.fetchone()

    if not result:
        print("Produto não encontrado.")
        return

    nome = result[0]
    confirm = input(f"Tem certeza que deseja deletar o produto '{nome}'? (s/n): ").lower()

    if confirm == "s":
        cursor.execute("DELETE FROM TB_Produtos WHERE id = %s", (produto_id,))
        conn.commit()
        print(f"Produto '{nome}' deletado com sucesso!")
    else:
        print("Operação cancelada.")


def interface():
    while True:
        print("\n" + "-"*20)
        print("1 | Criar Tabela de Usuário")
        print("2 | Criar Tabela de Produto")
        print("3 | Cadastrar Usuário")
        print("4 | Cadastrar Produto")
        print("5 | Listar Produtos")
        print("6 | Editar Produto")
        print("7 | Vender Produto")
        print("8 | Excluir Produto")
        print("9 | Sair")
        op = input("Escolha uma opção: ")

        match op:
            case "1":
                criar_tabela_pes()
            case "2":
                criar_tabela_prod()
            case "3":
                cadastrar_usuario()
            case "4":
                cadastro_produto()
            case "5":
                listar_produtos()
            case "6":
                editar_produto()
            case "7":
                vender_produto()
            case "8":
                deletar_produto()
            case "9":
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")

# --- INÍCIO DO PROGRAMA ---
login()
