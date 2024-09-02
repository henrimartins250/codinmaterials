
package com.mycompany.projeto_b;
public class Projeto_b {
     public static void main(String[] args) {
 Aluno alu1 = new Aluno();

 // Métodos da Superclasse
 alu1.setNome("Toto");
 alu1.setLogin("toto123");
 alu1.setSenha(1234);
 alu1.setEmail("toto@gmail.com");
 // Métodos da Subclasse
 alu1.setCurso("Desenvolvimento de Sistemas");
 alu1.setSerie(1);

 // Mostrar os dados
 alu1.verDados();
 }
}
