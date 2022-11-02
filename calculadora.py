
def soma(a, b):
    resultado = a + b
    return print(f'\n{a} + {b} = {resultado}')

def sub(a, b):
    resultado = a - b
    return print(f'\n{a} - {b} = {resultado}')

def mult(a, b):
    resultado = a * b
    return print(f'\n{a} * {b} = {resultado}')

def div(a, b):
    resultado = a / b
    return print(f'\n{a} / {b} = {resultado}')

def menu():
    calculadora = 'Calculadora'
    print(calculadora.center(50, '-'))  

    print('Informe qual será o tipo de operacao:\n')
    print('1 - Soma')
    print('2 - Subtracao')
    print('3 - Multiplicacao')
    print('4 - Divisao')
    print('5 - Sair')

menu()
operacao = int(input('\n'))

while operacao >= 1 and operacao <= 4:
    if operacao == 1:
        num1 = int(input("\nInforme o primeiro numero: "))    
        num2 = int(input("Informe o segundo numero: "))
        soma(num1, num2)  
    elif operacao == 2:
        num1 = int(input("\nInforme o primeiro numero: "))    
        num2 = int(input("Informe o segundo numero: "))
        sub(num1, num2)
    elif operacao == 3:
        num1 = int(input("\nInforme o primeiro numero: "))    
        num2 = int(input("Informe o segundo numero: "))
        mult(num1, num2)
    elif operacao == 4:
        num1 = int(input("\nInforme o primeiro numero: "))    
        num2 = int(input("Informe o segundo numero: "))
        if num2 == 0:
            print('\nImpossivel dividir por zero!')
        else:    
            div(num1, num2)
    else:
        print('\nOperacao invalida!')

    print('\n')    
    menu()
    operacao = int(input('\n'))
