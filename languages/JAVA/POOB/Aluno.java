package projeto_b;
public class Aluno extends Usuario {
 private String curso;
 private int serie;
 public Aluno(String curso, int serie, String login, int senha, String nome, int 
idade) {
 super(login, senha, nome, idade);
 this.curso = curso;
 this.serie = serie;
 }
 public Aluno(){
 
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
 
 @Override
 public void verDados(){
 super.verDados();
 System.out.println("Curso: " + this.curso);
 System.out.println("Serie: " + this.serie);
 }
 
 public boolean verificaAprovado(String mencao, double frequencia){
 if("I".equals(mencao)){
 return false;
 } else {
 if(frequencia < 0.75){
 return false;
 } else {
 return true;
 }
 }
 }
 
 public boolean verificaAprovado(double media, double frequencia){
 if(media < 6.0){
 return false;
 } else {
 if(frequencia < 0.75){
 return false;
 } else {
 return true;
 }
 }
}
}

