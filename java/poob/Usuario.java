
package com.mycompany.projeto_b;
public class Usuario {
    private String login;
 private int senha;
 private String nome;
 private String email;
 public Usuario(String login, int senha, String nome, String email) {
 this.login = login;
 this.senha = senha;
 this.nome = nome;
 this.email = email;
 }
 public Usuario(){
 this.login = "";
 this.senha = 0;
 this.nome = "";
 this.email = "";
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
 public String getEmail() {
 return email;
 }
 public void setEmail(String email) {
 this.email = email;
 }

 public void verDados(){
 System.out.println("\n----------------------------------");
 System.out.println("Nome: "+this.getNome());
 System.out.println("Login: "+this.getLogin());
 System.out.println("Senha: "+this.getSenha());
 System.out.println("E-mail: "+this.getEmail());
 }
}

