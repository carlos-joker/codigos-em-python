import sys,time,csv


lista = [[],[]]

def menu():
    print('-'*100 + '|')
    a = input('Digite o que deseja fazer : 1- Adicionar 2-listar 3- Pesquisar 4-Excluir 5-Alterar 6-Sair: ')
    print('-'*100 + '|')
    if a == '1':
        return adicionar()
    elif a == '2':
        return listar()
    elif a == '3':
        return pesquisar()
    elif a == '4':
        return excluir()
    elif a == '5':
        return alterar()
    elif a == '6':
        sys.exit()
    else:
        print('Opção Invalida!!!')
        return menu()

def adicionar():
    contato = str(input('\nDigite o nome do contato:\n'))
    a = contato in lista[0]
    if a == True:
        print('Já possui um contato com esse nome.')
        time.sleep(1)
        return adicionar()
    else:
        lista[0].append(contato.strip())
        
        

    time.sleep(1)
    numero = input('Digite o número do contato:\n')
    lista[1].append(numero)
    time.sleep(1)
    print('Adicionado com sucesso\n')
    return menu()

def listar():
    
    print('\n')
    for i in range (len(lista[0])):
        print('Nome: {}  Número: {} '.format(lista[0][i], lista[1][i]))
  
    a = False
    while True:
        if not lista[0]:
            print('Não há contatos.\n')
            time.sleep(1)
            a
            return menu()
        else:
            print('\n')
            time.sleep(1)
            a
            return menu()
           

def pesquisar():
    nome = str(input('\nDigite o nome desejado: '))
    print('Buscando...')
    time.sleep(1.5)
    for i in range (len(lista[0])):
        if nome == lista[0][i]:
            print('PESQUISA CONCLUÍDA COM SUCESSO\n')
            print('Nome: {}  Número: {}\n '.format(lista[0][i], lista[1][i]))
            time.sleep(1)
            return menu()
    if nome != lista[0]:
        print('PESQUISA CONCLUÍDA COM SUCESSO\n')
        print('Não consta um contato com esse nome!!!\n')
        time.sleep(1)
        return menu()
    
    
            
def excluir():
    nome = str(input('Digite o nome que deseja remover: '))
    print('Buscando...')
    time.sleep(1)
    for i in range(len(lista[0])):
        if nome == lista[0][i]:
            x = input('Deseja realmente excluir o contato? (s/n)')
            if x.lower() == 's':
                lista[0].pop(i)
                lista[1].pop(i)
                print('Contato removido com sucesso!!!\n')
                time.sleep(1)
                return menu()
            elif x.lower() == 'n':
                print('Cancelando operação!!!\n')
                time.sleep(1)
                return menu()
    if nome != lista[0]:
        print('PESQUISA CONCLUÍDA COM SUCESSO\n')
        print('Não consta um contato com esse nome!!!\n')
        time.sleep(1)
        return menu()

def alterar():
    nome = str(input('\nDigite o nome que deseja alterar: '))    
    for i in range(len(lista[0])):
        if nome == lista[0][i]:
            opcao = int(input('O que deseja alterar? 1- Nome 2- numero: '))  
            if opcao == 1:
                count = 1
                while count == 1:
                    nom = str(input('\nDigite o novo nome: '))
                    a = nom in lista[0]
                    if a == True:
                        print('O nome que você digitou é o mesmo ou ja existe um nome igual na lista')
                        print('Por favor, digite outro nome!!!')
                        count = 1
                    else:
                        lista[0][i] = nom
                        print('Nome alterado com sucesso!!!\n')
                        time.sleep(1)
                        return menu()   
            elif opcao == 2:
                num = int(input('\nDigite o novo numero: '))
                lista[1][i] = num
                print('Numero alterado com sucesso!!!\n')
                time.sleep(1)
                return menu()
        elif nome not in lista[0]:
            print('PESQUISA CONCLUÍDA COM SUCESSO\n')
            print('Não consta um contato com esse nome!!!\n')
            time.sleep(1)
            return menu()
    


menu()