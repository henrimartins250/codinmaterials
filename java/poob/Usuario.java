package projeto_b;
public class Usuario {
 private String login;
 private int senha;
 private String nome;
 private int idade;
 public Usuario(String login, int senha, String nome, int idade) {
 this.login = login;
 this.senha = senha;
 this.nome = nome;
 
 if(idade <18){
 this.idade = 0;
 } else {
 this.idade = idade; 
 }
 }
 
 public Usuario(){
 }
 
 public int getIdade() {
 return idade;
 }
 public void setIdade(int idade) {
 if(idade <18){
 this.idade = 0;
 } else {
 this.idade = idade; 
 }
 }
 public String getLogin() {
 return login;
 }
 public void setLogin(String login) {
 this.login = login;
 }
 public int getSenha() {
 return senha;
 }
 public void setSenha(int senha) {
 this.senha = senha;
 }
 public String getNome() {
 return nome;
 }
 public void setNome(String nome) {
 this.nome = nome;
 }
 public void verDados(){
 System.out.println("===============================-");
 System.out.println("Nome: "+this.getNome());
 System.out.println("Login: "+this.getLogin());
 System.out.println("Senha: "+this.getSenha());
 System.out.println("Idade: "+this.getIdade());
 } 
}
