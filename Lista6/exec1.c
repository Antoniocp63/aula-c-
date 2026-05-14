// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int numeros[10];
    int pos;
 
 for (pos = 0; pos < 10; pos++){
     printf("Digite o número da posição %d: ", pos);
     scanf("%d", &numeros[pos]);
 }
     printf("Valores digitados %d: ", pos);
     for (pos = 0; pos < 10; pos++){
         printf("numeros[%d] = %d\n", pos, numeros[pos]);
 }
    return 0;
}