programa {
  funcao inicio() {
    inteiro somapar = 0, somaimpar = 0, numero, contador
    logico switch = falso
    
escreva("DIGITE SEU NUMERO:")
leia(numero)

    enquanto(switch == falso){
    para (contador = 0; contador <= numero; contador++ ){
      se((contador % 2)== 0)
      somapar = somapar + contador
      senao{
        switch = verdadeiro
      }
    }
    }

    enquanto(switch == verdadeiro){
    para (contador = 0; contador <= numero; contador++ ){
      se((contador % 2)== 1)
      somaimpar = somaimpar + contador
      senao{
        switch = falso
      }
    }
    }



    escreva("soma impares" ,somaimpar, "\n")
    escreva("soma pares" ,somapar, "\n")
  }
}
