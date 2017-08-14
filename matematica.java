public class Matematica
{ // corpo da classe
 
  public static int a, b; // atributos da classe
 
// adicao, subtracao, multiplicacao e divisao representam o "protocolo"
// de métodos implementados pela classe Matematica.
  public static int adicao() {
    return (a + b);
  }
 
  public static int subtracao() {
    return (a - b);
  }
 
  public static int multiplicacao() {
    return (a * b);
  }
 
  public static int divisao() {
    return (a / b);
  }
 public static int teste() {
   if (a == 0){
     a = 1;
   }
   if (b == 0){
     b = 1
   }
    return ((a / b))/2;
  }
} // fim do corpo da classe "Matematica"