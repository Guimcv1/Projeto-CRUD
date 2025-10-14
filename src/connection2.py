from main import get_connect
from passlib.hash import pbkdf2_sha256 as crypto



def criar_usuario(nome, email, senha):
    try:
        conn = get_connect()
        cursor = conn.cursor()

        cursor.execute('INSERT INTO TB_USUARIO(nome, email, senha)VALUES (?,?,?)',
                       (nome, email, senha)
        )
        conn.commit()
        print('Usuario cadastrado com sucesso!') 
    except Exception as e:
            print(f'Falha ap criar uma tabela: {e}')
def listar_usuario():
     try: 
          conn = get_connect()
          cursor = conn.cursor()
          cursor.execute('SELECT * FROM TB_Usuario')
          usuarios = cursor.fetchall()
          
          if usuarios:
               print(f'{30*'-'}LIsata de usuarios{30*'-'}')
               for u in usuarios:
                    print(f'|{u}')
          else:
               print('Nenhum usuario cadastrado!')
               return

     except Exception as e:
          print(f'Falha ao listar usuario: {e}')
     

def excluir_usuario(ID):
    ...

def editar_usuario(ID):
     ...

def listar_usuario_email(EMAIL):
     ...

def listar_usuario_ID(ID):
     ...
def criar_tabela():
    try:
          conn = get_connect()
          cursor = conn.cursor()

          cursor.execute('''
          CREATE TABLE TB_Usuario(
            ID INTEGER PRIMARY KEY,
            NOME VARCHAR(120) NOT NULL,
            EMAIL VARCHAR(120) UNIQUE,
            SENHA VARCHAR(255)
          );
    ''')
    except Exception as e:
            print(f'Falha ap criar uma tabela: {e}')

if __name__ == '__main__':
     #criar_tabela()
     nome = input('Digite um nome: ').strip().title()
     email = input('Digite um email: ').strip()
     senha = input('Digite uma senha: ').strip()

criar_usuario(nome, email, senha) 