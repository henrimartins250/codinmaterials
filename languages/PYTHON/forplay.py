amigos = ["ian", "rafael", "enrico"]

for indice, amigo in enumerate(amigos):
  print(indice, amigo)



#-----------------------------------------------------------------------------

vetorf = [6, 8, 6, 4, 9]
soma = int(0)
mult = int(1)

#for i in range(5):
 #   vetorf.append(int(input("digite o valor:")))

for numeros in vetorf:
  soma += numeros
  mult += (mult * numeros)

    

    


print(vetorf)
print(soma)
print(mult)


#--------------------------------------------------------------------------

listaf =[4, 9, 8, 2, 6,]
sroot =()
for nomeros in listaf:
  sroot = nomeros*nomeros
  print(sroot)


#-------------------------------------------------------------------

listat = [37, 68, 7, 546, 572, 876, 98]
lista = []

lista += listat
lista.sort()
max = lista[-1]

for indic, listo in enumerate(listat):
  if listo == max:
       print(indic, listo)

#-----------------------------------------------------------------------------------  


lista = [37, 68, 7, 546, 572, 876, 98]

max = int(0)

for indic, listo in enumerate(lista):
  if listo > max:
    max = listo
    max_indic = indic

print(max, max_indic)

#--------------------------------------------------------------------------------------

frotas = ["bananya", "laranjya", "kiywa", "umbuya"]

for posicao, fruta in enumerate(frotas):
  print(posicao, fruta)



#------------------------------------------------------------------------------------------



amigos = ["ian", "rafael", "enrico"]

for indice, amigo in enumerate(amigos):
  print(indice, amigo)



#------------------------------------------------------------------------------------------------


jogos = ["cod", "gow", "lol"]
notas = [9, 7, 3]
for i, jogo in enumerate(jogos):    
  print(jogo, notas[i])
