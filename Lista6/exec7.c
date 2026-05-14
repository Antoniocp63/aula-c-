// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int numeros[8];
    int pos;
    
   for (pos = 0; pos < 8; pos++){
     printf("Digite o número da posição %d: ", pos);
     scanf("%d", &numeros[pos]);
 }
    printf("Valores em ordem inversa");
    for (pos = 7; pos >= 0; pos--){
        printf("%d\n", numeros[pos]);
    }
    
    return 0;
}