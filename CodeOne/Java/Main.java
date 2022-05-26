public class Main {

  public static void main(String[] args) {

    // Exemplo de uso de variáveis do tipo string

    String nome;
    nome = "Let's Code";
    nome = "Fernanda";
    nome = "Brasil";
    System.out.println("Olá, " + nome);

    // Exemplo de uso de variáveis numéricas

    int a;
    int b = 5;
    a = 4;
    int soma = a + b;
    int subtracao = a - b;
    int multiplicacao = a * b;
    float divisao = (float) a / b;

    System.out.println(soma);
    System.out.println(subtracao);
    System.out.println(multiplicacao);
    System.out.println(divisao);

    // Exemplo de uso de operadores booleanos

    boolean resultado = true;
    System.out.println(resultado);

    // Algoritmo ida à praia

    boolean fimDeSemana = true;
    boolean fazendoSol = true;
    boolean vamosAPraia = fimDeSemana && fazendoSol;

    System.out.println(vamosAPraia);

    // Tabela Verdade

    // Operador && (AND)
    // true && true = true
    // true && false = false
    // false && true = false
    // false && false = false

    // Operador || (OR)
    // true || true = true
    // true || false = true
    // false || true = true
    // false || false = false

    // Uso do operador ternário (?)
    // O operador ternário avalia se um item lógico é verdadeiro ou não.
    // Dependendo do resultado o operador ternário traz um retorno diferente.

    String mensagem = fimDeSemana ? "É fim de semana! :D" : "Não é fim de semana! :(";
    System.out.println(mensagem);
  }
}