programa {
  funcao inicio() {
    inteiro num
    cadeia sexo, fe, ma, in

     para (num = 0; num <= 10; num++ ){
    leia(sexo)
    se(sexo == fe){
      fe++
    }
    senao se(sexo == ma){
      ma++
    }
    senao{
      in++
    }

    }
    

escreva("masculina\t",ma)
escreva("",fe)
escreva("",in)
  }
}
