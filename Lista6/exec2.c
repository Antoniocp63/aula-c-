// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int numeros[8];
    int pos, soma = 0;
    
    for (pos = 0; pos < 8; pos++){
     printf("Digite o número da posição %d: ", pos);
     scanf("%d", &numeros[pos]);
    }
     for (pos = 0; pos < 8; pos++){
         soma += numeros[pos];
     }
     
    printf("a soma foi igual a %d", soma);
    return 0;
}