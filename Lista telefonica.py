import sys,time

lista = [[],[]]


def menu():
    a = int(input('Digite o que deseja fazer : 1- Adicionar 2-listar 3- Pesquisar 4-Excluir 5-Alterar 6-Sair: '))
    if a == 1:
        return adicionar()
    elif a == 2:
        return listar()
    elif a == 3:
        return pesquisar()
    elif a == 4:
        return excluir()
    elif a == 5:
        return alterar()
    elif a == 6:
        sys.exit()
    else:
        print('Opção Invalida!!!')
        return menu()

def adicionar():
    contato = str(input('Digite o nome do contato:\n'))
    lista[0].append(contato)
    time.sleep(1.5)
    numero = int(input('Digite o número do contato:\n'))
    lista[1].append(numero)
    time.sleep(1.5)
    print('Adicionado com sucesso')
    return menu()


def listar():

    
    for i in range (len(lista[0])):
        print('Nome: {}  Número: {} '.format(lista[0][i], lista[1][i]))
    
    return menu()

def pesquisar():
    nome = str(input('Digite o nome desejado: '))
    for i in range (len(lista[0])):
        if nome == lista[0][i]:
            print(lista[0][i], lista[1][i])
            return menu()
        else:
            print('Não consta um contato com esse nome!!! ')
    return menu()
            
def excluir():
    nome = str(input('Digite o nome que deseja remover: '))
    for i in range(len(lista[0])):
        if nome == lista[0][i]:
            x = input('Deseja realmente excluir o contato? (s/n)')
            if x.lower() == 's':
                lista[0].pop(i)
                lista[1].pop(i)
                print('Contato removido com sucesso!!!')
                return menu()
            elif x.lower() == 'n':
                print('Cancelando operação!!!')
                return menu()

def alterar():
    nome = str(input('Digite o nome que deseja alterar: '))    
    for i in range(len(lista[0])):
        if nome == lista[0][i]:
            opcao = int(input('O que deseja alterar? 1- Nome 2- numero: '))  
            if opcao == 1:
                nom = str(input('Digite o novo nome: '))
                lista[0][i] = nom
                print('Nome alterado com sucesso!!!')
                return menu()   
            elif opcao == 2:
                num = int(input('Digite o novo numero: '))
                lista[1][i] = num
                print('Numero alterado com sucesso!!!')
                return menu()
    
    


menu()
