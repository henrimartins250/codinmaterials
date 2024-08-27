carrinho = []
quant = int()
item = str 


print("escreva os itens que você colocou em seu caarrinho")
carrinho.append(input("escreva: "))
carrinho.append(input("escreva: "))
carrinho.append(input("escreva: "))
carrinho.append(input("escreva: "))
quant = (len(carrinho))
print(carrinho)
print(quant)
if quant > 3:
    print(" nao pode")

else:
    print("pode passar")


