// Online C compiler to run C program online
#include <stdio.h>

int main() {
   int i, numero, soma;
   for (i = 1; i < 5; i++) {
       scanf("%d" , &numero);
       if (numero > 0){
           soma = soma + numero;
       }
   }
    printf("Soma: %d\n", soma);
    return 0;
}