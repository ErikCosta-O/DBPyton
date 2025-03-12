import sqlite3
import os  # Para manipular o sistema de arquivos

caminho = r'C:\Users\ERIK\Documents\DBPyton\contatos.db'  # Caminho do arquivo

# Perguntar ao usuário se deseja excluir o banco de dados existente
if os.path.exists(caminho):
    opcao = input("Deseja excluir o banco de dados existente? (S/N): ")
    if opcao.upper() == 'S':
        try:
            os.remove(caminho)  # Excluir o arquivo existente
            print("Arquivo 'contatos.db' excluído com sucesso 👍.")
        except OSError as e:
            print(f"Erro ao excluir o arquivo: {e}")
    else:
        print("O banco de dados existente será mantido.")
else:
    print("O arquivo 'contatos.db' não existe. Um novo será criado.")

try:
    # Criar um novo banco de dados
    con = sqlite3.connect(caminho)
    print("Novo banco de dados 'contatos.db' criado com sucesso.")

    # Criando a tabela no banco
    vsql = """CREATE TABLE IF NOT EXISTS tb_contatos
        (ID_CONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME_CONTATO CHAR,
        TELEFONE_CONTATO CHAR,
        E_MAIL_CONTATO CHAR)"""
    try:
        c = con.cursor()
        c.execute(vsql)
        print("A tabela foi criada com sucesso.")
    except sqlite3.OperationalError as ex:
        print(f"Erro ao criar a tabela: {ex}")

except sqlite3.Error as ex:
    print(f"Erro na conexão com o Banco de Dados: {ex}")

finally:
    if 'con' in locals() and con:
        con.close()
        print("Conexão fechada com sucesso.")

def menuprincipal():
    opc = 0
    while opc != 6:
        os.system("cls")
        print("1 - Inserir novo registro")
        print("2 - Deletar registro")
        print("3 - Atualizar registro")
        print("4 - Consultar registro")
        print("5 - Consultar Registro por nome")
        print("6 - Sair")

        try:
            opc = int(input("Digite uma opção: "))
        except ValueError:
            print("Opção inválida. Por favor, digite um número.")
            os.system("pause")
            continue

        if opc == 1:
            menuinserir()
        elif opc == 2:
            menudeletar()
        elif opc == 3:
            menuatualizar()
        elif opc == 4:
            menuconsultar()
        elif opc == 5:
            menuconsultar_nome()
        elif opc == 6:
            os.system("cls")
            print("Programa finalizado.")
        else:
            os.system("cls")
            print("Opção inválida.")
            os.system("pause")

def menuinserir():
    os.system("cls")
    vnome = input("Digite o nome do contato: ")
    vtelefone = input("Digite o telefone do contato: ")
    vemail = input("Digite o e-mail do contato: ")
    caminho = r'C:\Users\ERIK\Documents\DBPyton\contatos.db'
    try:
        con = sqlite3.connect(caminho)
        cur = con.cursor()
        cur.execute("INSERT INTO tb_contatos (NOME_CONTATO, TELEFONE_CONTATO, E_MAIL_CONTATO) VALUES (?, ?, ?)", (vnome, vtelefone, vemail))
        con.commit()
        print("Registro inserido com sucesso.")
    except sqlite3.Error as ex:
        print(f"Erro ao inserir registro: {ex}")
    finally:
        if 'con' in locals() and con:
            con.close()
            print("Registro inserido com sucesso.")
        os.system("pause")

def menudeletar():
    os.system("cls")
    caminho = r'C:\Users\ERIK\Documents\DBPyton\contatos.db'
    try:
        v_id_contato = int(input("Digite o ID do contato que deseja deletar: "))
        con = sqlite3.connect(caminho)
        cur = con.cursor()
        cur.execute("SELECT * FROM tb_contatos WHERE ID_CONTATO = ?", (v_id_contato,))
        r = cur.fetchall()
        if len(r) > 0:
            print("\n++++++++++++++ Contato Encontrado ++++++++++++++")
            print(f"ID      : {r[0][0]}")
            print(f"Nome    : {r[0][1]}")
            print(f"Telefone: {r[0][2]}")
            print(f"E-mail  : {r[0][3]}")
            print("++++++++++++++++++++++++++++++++++++++++++++++++\n")
            print("Registro consultado com sucesso.")
            decide = input("Deseja realmente deletar este registro? (S/N): ")
            if decide.upper() == "S":
                try:
                    v_sql_deleta = "DELETE FROM tb_contatos WHERE ID_CONTATO = ?"
                    cur.execute(v_sql_deleta, (v_id_contato,))
                    con.commit()
                    print("Registro deletado com sucesso.")
                except sqlite3.Error as ex:
                    print(ex)
                finally:
                    os.system("pause")
            else:
                print("Registro não deletado.")
                os.system("pause")
        else:
            print("Registro não encontrado.")
            os.system("pause")
    except sqlite3.Error as ex:
        print(ex)
        os.system("pause")
    finally:
        con.close()

def menuatualizar():
    os.system("cls")
    caminho = r'C:\Users\ERIK\Documents\DBPyton\contatos.db'
    try:
        v_id_contato = int(input("Digite o ID do contato que deseja atualizar: "))
        con = sqlite3.connect(caminho)
        cur = con.cursor()
        cur.execute("SELECT * FROM tb_contatos WHERE ID_CONTATO = ?", (v_id_contato,))
        r = cur.fetchall()
        if len(r) > 0:
            print("ID : {0: <3} Nome: {1: <30} Telefone: {2: <17} E-mail: {3: <30}".format(r[0][0], r[0][1], r[0][2], r[0][3]))
            print("Registro consultado com sucesso.")
            vnome = input("Digite o novo nome do contato: ")
            if len(vnome) == 0:
                vnome = r[0][1]
            
            vtelefone = input("Digite o novo telefone do contato: ")
            if len(vtelefone) == 0:
                vtelefone = r[0][2]
            
            vemail = input("Digite o novo e-mail do contato: ")
            if len(vemail) == 0:
                vemail = r[0][3]
            
            print("\n++++++++++++++ Novos Dados ++++++++++++++")
            print(f"ID      : {r[0][0]}")
            print(f"Nome    : {vnome}")
            print(f"Telefone: {vtelefone}")
            print(f"E-mail  : {vemail}")
            print("++++++++++++++++++++++++++++++++++++++++\n")
            
            decide = input("Deseja realmente atualizar este registro? (S/N): ")
            if decide.upper() == "S":
                try:
                    v_sql_atualiza = "UPDATE tb_contatos SET NOME_CONTATO = ?, TELEFONE_CONTATO = ?, E_MAIL_CONTATO = ? WHERE ID_CONTATO = ?"
                    cur.execute(v_sql_atualiza, (vnome, vtelefone, vemail, v_id_contato))
                    con.commit()
                except sqlite3.Error as ex:
                    print(ex)
                finally:
                    print("Registro atualizado com sucesso.")
                    os.system("pause")
            else:
                print("Registro não atualizado.")
                os.system("pause")
        else:
            print("Registro não encontrado.")
            os.system("pause")
    except sqlite3.Error as ex:
        print(ex)
        os.system("pause")
    finally:
        con.close()

def menuconsultar():
    os.system("cls")
    caminho = r'C:\Users\ERIK\Documents\DBPyton\contatos.db'
    try:
        con = sqlite3.connect(caminho)
        cur = con.cursor()
        cur.execute("SELECT * FROM tb_contatos")
        r = cur.fetchall()
        vlimite = 10
        vcont = 0
        print("\n++++++++++++++ Lista de Contatos ++++++++++++++")
        for r in r:
            print(f"ID      : {r[0]}")
            print(f"Nome    : {r[1]}")
            print(f"Telefone: {r[2]}")
            print(f"E-mail  : {r[3]}")
            print("++++++++++++++++++++++++++++++++++++++++++++++\n")
            vcont += 1
            if vcont >= vlimite:
                vcont = 0
                os.system("pause")
                os.system("cls")
                print("\n++++++++++++++ Lista de Contatos ++++++++++++++")
        print("Fim da lista.")
        print("Registros consultados com sucesso.")
        os.system("pause")
    except sqlite3.Error as ex:
        print(ex)
        os.system("pause")
    finally:
        con.close()

def menuconsultar_nome():
    os.system("cls")
    caminho = r'C:\Users\ERIK\Documents\DBPyton\contatos.db'
    try:
        vnome = input("Digite o nome do contato que deseja consultar: ")
        con = sqlite3.connect(caminho)
        cur = con.cursor()
        cur.execute("SELECT * FROM tb_contatos WHERE NOME_CONTATO LIKE ?", ('%' + vnome + '%',))
        r = cur.fetchall()
        if len(r) > 0:
            print("\n++++++++++++++ Contatos Encontrados ++++++++++++++")
            for r in r:
                print(f"ID      : {r[0]}")
                print(f"Nome    : {r[1]}")
                print(f"Telefone: {r[2]}")
                print(f"E-mail  : {r[3]}")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            print("Registros consultados com sucesso.")
        else:
            print("Nenhum registro encontrado.")
        os.system("pause")
    except sqlite3.Error as ex:
        print(ex)
        os.system("pause")
    finally:
        con.close()

if __name__ == "__main__":
    menuprincipal()