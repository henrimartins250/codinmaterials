import math

def subtraction(n1, n2):
    return n1 - n2

def addition(n1, n2):
    return n1 + n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 == 0:
        return "Error: Divisão por zero"
    return n1 / n2

def exponentiation(n1, n2):
    return n1 ** n2

def squareroot(n1):
    if n1 < 0:
        return "Error: nao é possivel encontrar a raiz quadrada de um numero negativo "
    return math.sqrt(n1)

lip = True  

while lip:
    try:
        n1 = float(input("\nDigite o seu primeiro número: "))
        n2 = float(input("\nDigite o seu segundo número: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue

    esc = input("Esses são os comandos que você pode realizar:\n"
                "s: subtração;\n"
                "a: adição;\n"
                "m: multiplicação;\n"
                "d: divisão;\n"
                "e: exponenciação;\n"
                "r: raiz quadrada;\n"
                "ou digite (sair) para parar \n"
                "Qual operação você deseja fazer: ")

    match esc:
        case "s":
            result = subtraction(n1, n2)
            print(f"Resultado da subtração: {result}")
        case "a":
            result = addition(n1, n2)
            print(f"Resultado da adição: {result}")
        case "m":
            result = multiplication(n1, n2)
            print(f"Resultado da multiplicação: {result}")
        case "d":
            result = division(n1, n2)
            print(f"Resultado da divisão: {result}")
        case "e":
            result = exponentiation(n1, n2)
            print(f"Resultado da exponenciação: {result}")
        case "r":
            result = squareroot(n1)
            print(f"Resultado da raiz quadrada: {result}")
        case "sair":
            print("Tchauzinho!")
            lip = False
        case _:
            print("Comando não reconhecido. Tente novamente.")
        
