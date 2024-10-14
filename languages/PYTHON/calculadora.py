import math
n1 = ()
n2 = ()

def subtraction(n1, n2):
    return n1 - n2

def addition(n1, n2):
    return n1 + n2

def multiplication(n1, n2):
   return n1 * n2

def division(n1, n2):
   return n1 / n2

def exponetiation(n1, n2):
    return n1 ** n2

def squareroot(n1, n2):
    math.sqrt(n1)

lip = True  

while lip == True:
  n1 = int(input("digite o seu primeiro numero"))
  n2 = int(input("digite o seu primeiro numero"))
  esc = input("esses são os camandos que voce pode realizar:\n s: subtração;\n a: adição;\n m: multiplacação;\nd: divisão;\ne: exponeciação;\n r: raiz quadrada;\nou digite (sair) para parar \nqual operação voce deseja fazer")
  match esc:
    case ("s"):
      subtraction(n1, n2)
    case "a":
      addition(n1, n2)
    case "m":
      multiplication(n1, n2)
    case "d":
      division(n1, n2)
    case "e":
      exponetiation(n1, n2)
    case "r":
      squareroot(n1)
    case "sair":
      print("tchauzinho")
      lip = False  
