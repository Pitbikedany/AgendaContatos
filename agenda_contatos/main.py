from connection import *
from tabulate import tabulate
import os
def limpar():
    os.system('cls')
def pausar():
    pausa = input('Pressione ENTER para continuar...')

while True:
    print('''
    L - Listar Contatos
    E - Eliminar Contatos
    A - Alterar Contatos
    V - Ver Contatos
    F - Fechar Programa
    ''')
    escolha = input('Escolha uma opção: ')
    limpar()

    if escolha == 'L' or escolha == 'l':
        info=[]
        nome = input('Nome: ')
        info.append(nome)
        numero = input('Número: ')
        info.append(numero)
        email = input('Email: ')

        if email == '':
            email = 'null'
        info.append(email)
        try:
            add_contatos = f"INSERT INTO contatos(nome,numero,email) VALUES('{nome}','{numero}','{email}')"
            myqueries.execute(add_contatos)
            mydatabase.commit()
            print('Contato adicionado com sucesso')
        except:
            print('Ocorreu um erro, tente mais tarde')
        pausar()
        limpar()

    elif escolha == 'E' or escolha == 'e':

        while True:
            myqueries.execute("SELECT * FROM contatos")
            show_contatos = myqueries.fetchall()
            nomes = []
            numeros = []
            emails = []
            for values in show_contatos:
                nomes.append(values[0])
                numeros.append(values[1])
                emails.append(values[2])

            table = [
                ["ID","Nome","Numero","Email"]
            ]
            i = 0
            while i < len(nomes):
                info = [i,nomes[i], numeros[i], emails[i]]
                i += 1
                table.append(info)
        
            print(tabulate(table,headers="firstrow",tablefmt="pretty"))
            delete_id = int(input('Indique o ID que deseja eliminar: '))
            try:
                myqueries.execute(f"DELETE FROM contatos WHERE numero='{numeros[delete_id]}'")
                mydatabase.commit()
                print('Contato eliminado com sucesso')
                pausar()
                break
            except:
                print('Ocorreu um erro, tente novamente')
            limpar()

    elif escolha == 'V' or escolha == 'v':
        myqueries.execute("SELECT * FROM contatos")
        show_contatos = myqueries.fetchall()
        nomes = []
        numeros = []
        emails = []
        for values in show_contatos:
            nomes.append(values[0])
            numeros.append(values[1])
            emails.append(values[2])

        table = [
            ["Nome","Numero","Email"]
        ]
        i = 0
        while i < len(nomes):
            info = [nomes[i], numeros[i], emails[i]]
            i += 1
            table.append(info)
    
        print(tabulate(table,headers="firstrow",tablefmt="pretty"))
        pausar()
        limpar()

    elif escolha == 'A' or escolha == 'a':
        break_while = False
        while True:
            myqueries.execute("SELECT * FROM contatos")
            show_contatos = myqueries.fetchall()
            nomes = []
            numeros = []
            emails = []
            for values in show_contatos:
                nomes.append(values[0])
                numeros.append(values[1])
                emails.append(values[2])

            table = [
                ["ID","Nome","Numero","Email"]
            ]
            i = 0
            while i < len(nomes):
                info = [i,nomes[i], numeros[i], emails[i]]
                i += 1
                table.append(info)
        
            print(tabulate(table,headers="firstrow",tablefmt="pretty"))
            update_id = int(input('Indique o ID que deseja alterar: '))
            while True:
                print('''
                    1 - Nome
                    2 - Numero
                    3 - Email
                    F - Fechar
                    ''')
                escolha_alterar = input('Escolha a opção que deseja alterar: ')
                if escolha_alterar == '1':
                    new_name = input('Nome:')
                    try:
                        myqueries.execute(f"UPDATE contatos SET nome = '{new_name}' WHERE numero='{numeros[update_id]}'")
                        mydatabase.commit()
                        print('Contato alterado com sucesso')
                        pausar()
                    except:
                        print('Ocorreu um erro, tente novamente')

                elif escolha_alterar == '2':
                    new_numero = input('Numero:')
                    try:
                        myqueries.execute(f"UPDATE contatos SET numero = '{new_numero}' WHERE numero='{numeros[update_id]}'")
                        mydatabase.commit()
                        print('Contato alterado com sucesso')
                        pausar()
                    except:
                        print('Ocorreu um erro, tente novamente')

                elif escolha_alterar == '3':
                    new_email = input('Email:')
                    try:
                        myqueries.execute(f"UPDATE contatos SET email = '{new_email}' WHERE numero='{numeros[update_id]}'")
                        mydatabase.commit()
                        print('Contato alterado com sucesso')
                        pausar()
                        limpar()
                    except:
                        print('Ocorreu um erro, tente novamente')

                elif escolha_alterar == 'F' or escolha_alterar =='f':
                    break_while = True
                    break

                else: 
                    print('Opção errada...')
            if break_while:
                break
    elif escolha == 'F' or escolha == 'f':
        break
    else: 
        print('Opção Inválida...')