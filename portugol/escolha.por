programa {
  funcao inicio() {
    
    inteiro idade, seila

    escreva("digite a sua idade\n")
    leia(idade)

    

    se(idade <= 4)
    seila = 1
    senao se(idade > 4 e idade <= 7)
    seila = 2
    senao se(idade > 7 e idade <= 10)
    seila = 3
    senao se(idade > 10 e idade <= 13)
    seila = 4
    senao se(idade > 13 e idade <= 17)
    seila = 5
    senao se(idade > 17)
    seila = 6
    senao
    seila = -1


escolha(seila){
  caso 1:
    escreva("nao aceito\n")
      pare
  caso 2:
    escreva("infantil A")
      pare
  caso 3:
    escreva("infantil B")
      pare
  caso 4:
    escreva("juvenil A")
      pare
  caso 5:
    escreva("juvenil B")
      pare
  caso 6:
    escreva("sênior")
      pare
  caso contrario:
    escreva("invalido")
      pare
  
  
}
     
  }
}
