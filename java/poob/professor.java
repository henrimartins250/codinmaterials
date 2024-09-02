package poo_x;
public class Professor extends Usuario{
 private String formacao;
 private double hora_aula;
 public Professor(String formacao, double hora_aula, String login, int senha, 
String nome, int idade) {
 super(login, senha, nome, idade);
 this.formacao = formacao;
 this.hora_aula = hora_aula;
 }
 
 public Professor(){
 }
 public String getFormacao() {
 return formacao;
 }
 public void setFormacao(String formacao) {
 this.formacao = formacao;
 }
 public double getHora_aula() {
 return hora_aula;
 }
 public void setHora_aula(double hora_aula) {
 this.hora_aula = hora_aula;
 }
 public void verDados(){
 super.verDados();
 System.out.println("Formação: " + this.formacao);
 System.out.println("Hora/Aula: "+ this.hora_aula);
 }
}
