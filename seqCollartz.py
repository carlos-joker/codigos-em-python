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
    print('\nTamanho da lista: {} numeros'.format(len(lista)))
    a = input('Deseja fazer um novo calculo? (s/n)')
    if a.lower() == 's':
        print('\n')
        return menu()
    else:
        print('Encerrando...')
    
def menu():
    try:
        number = int(input('Digite um numero positivo  e diferente de zero: '))
        if number < 0:
            print('Você digitou um numero negativo!!!')
            print('tente novamente.')
            return menu()
        elif number == 0:
            print('Você digitou um valor zero!!!')
            print('tente novamente.')
            return menu()
        else:
            return collatz(number)
    except:
        print('Você não digitou um número!!!')
        return menu()




menu()        