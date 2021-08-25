'''Sequência de Collatz
Crie uma função chamada collatz() que tenha um parâmetro de nome number.
Se number for par, collatz() deverá exibir number // 2 e retornar esse valor. Se
number for ímpar, collatz() deverá exibir e retornar 3 * number + 1.'''



def collatz(number):
    a = number
    lista = []
    lista.append(a)

    while a > 1:
        if a % 2 == 0:
            a = a // 2
            lista.append(a)              
        else:
            a = 3 * a + 1
            lista.append(a)
    print(lista)
    
def menu():
    try:
        number = int(input('Digite um numero: '))
        return collatz(number)
    except:
        print('Você não digitou um número!!!')
        return menu()




menu()        