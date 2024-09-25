programa {
  funcao inicio() {
   inteiro vetor[10], i

  escreva("digite 10 numeros:\n")
   para(i = 0; i <= 9; i++){
    leia(vetor[i])
   }
  para(i = 0; i <= 9; i++)
    se(vetor[i] < 0){
      vetor[i] = 0
    }
    para(i = 0; i <= 9; i++){
      escreva(vetor[i], "\t")
    }
  
  }
}
