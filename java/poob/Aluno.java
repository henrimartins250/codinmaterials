
package com.mycompany.projeto_b;

public class Aluno  extends Usuario{
     private String curso;
 private int serie;
 public Aluno(String curso, int serie, String login, int senha, String
nome, String email) {
 super(login, senha, nome, email);
 this.curso = curso;
 this.serie = serie;
 }
 public Aluno() {
 }
 public String getCurso() {
 return curso;
 }
 public void setCurso(String curso) {
 this.curso = curso;
 }
 public int getSerie() {
 return serie;
 }
 public void setSerie(int serie) {
 this.serie = serie;
 }

 public void verDados(){
 super.verDados();
 System.out.println("Curso: " + this.getCurso());
 System.out.println("Série: " + this.getSerie()+"ª");
 System.out.println("----------------------------------");
 }
}

   
