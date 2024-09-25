programa {

  inclua biblioteca Util --> u

  funcao inicio() {
  inteiro vetor[5] = {1, 2, 3, 4, 5}, menor = 0, i, maior = 0, pares[5] = {0 , 0 , 0 , 0 , 0}, impares[5] = {0 , 0 , 0 , 0 , 0}
  menor = vetor[0]

  escreva("digite 30 numeros:\n")
  para(i = 0; i <= 4; i++){
    se(vetor[i] > maior){
     maior = vetor[i]}
    senao se(vetor[i] < menor){
     menor = vetor[i]}
  }
  

  para(i = 0; i <= 4; i++){
    se(vetor[i] % 2 == 0){
      pares[i] = vetor[i]
    }
}
    para(i = 0; i <= 4; i++){
    se(vetor[i] % 2 == 1){
      impares[i] = vetor[i]
    }
  }
escreva("menor: ", menor, "maior: ", maior)


escreva("\n\npares: \n")
para(i = 0; i <= 4; i++){
  escreva(pares[i], "\t")
}


escreva("\n\nimpares: \n")
para(i = 0; i <= 4; i++){
  escreva(impares[i],"\t")
}

  }
}
