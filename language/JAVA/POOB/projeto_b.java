package projeto_b;
public class Projeto_b {
 public static void main(String[] args) {
 Aluno aluno1 = new Aluno();
 
 aluno1.setNome("Marco");
 aluno1.setLogin("mam222");
 aluno1.setSenha(7890);
 aluno1.setIdade(58);
 aluno1.setCurso("Desenvolvimento de Sistemas");
 aluno1.setSerie(1);
 
 aluno1.verDados();
 if(aluno1.verificaAprovado("MB", 0.9)){
 System.out.println("Aluno Aprovado");
 } else {
 System.out.println("Aluno Reprovado");
 }
 
 
 Aluno aluno2 = new Aluno("Administracao", 3, "xpto555", 5689,"Caio Rolando da 
Rocha", 22);
 aluno2.verDados();
 
 if(aluno2.verificaAprovado(7.2, 0.8)){
 System.out.println("Aluno Aprovado");
 } else {
 System.out.println("Aluno Reprovado");
 }
 
 Professor prof1 = new Professor();
 prof1.setNome("Marco");
 prof1.setLogin("toto123");
 prof1.setSenha(5555);
 prof1.setIdade(58);
 prof1.setFormacao("Mestre em Midias e Tecnologias");
 prof1.setHora_aula(35.0);
 
 prof1.verDados();
 
 }
 
}
