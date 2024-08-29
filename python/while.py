omg = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
par = []
impar = []
d = False

while d == False:
  for nue in omg:
    if (nue % 2) == 0:
      par.append(nue)
    else:
      d = True
while d == rue:
  for nue in omg:
    if (nue % 2) == 1:
      impar.append(nue)
    else:
      d = False
print(par)
print(impar)

-----------------------------------------------

nimirus = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
meno = int(1)
maio = int()
cc = False

while cc == False:
  for nuo in omg:
    if nuo > maio:
      maio = nuo
    else:
      cc = True
while cc == True:
  for nuo in omg:
    if nuo < meno :
      meno = nuo
    else:
      cc = False
print(meno)
print(maio)
