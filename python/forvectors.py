quant = []

for i in range(1,1001):
  if i % 2 ==0:
   quant.append(i)

print(len(quant))

----------------------------------------

import time

amigos = ["nicolas","pedros", "bruno" ]
for amigo in amigos:
  time.sleep(0.5)
  print(amigos)


----------------------------------------------

vetora = []
for i in range(5):
    vetora.append(int(input("digite o valor:")))

vetora.sort()
vetora.reverse()
print(vetora)

-----------------------------------

notas =[]
for i in range(4):
  notas.append(float(input("digite sua nota")))

media = (0)
for nota in notas:
  media += nota

print(media)

print(f"a media do aluno foi:{media / len(notas)}")

--------------------------------------------------------------

vetor =[]
vetorp=[]
vetori =[]

for i in range(10):
    vetor.append(int(input("digite o valor:")))
for item in vetor:
   if item % 2 ==0:
    vetorp.append(item)
   else:
    vetori.append(item)

print(vetor)
print(vetorp)
print(vetori)
