// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int numeros[10];
    int pos, maior;
    
for (pos = 0; pos < 10; pos++){
     printf("Digite o número da posição %d: ", pos);
     scanf("%d", &numeros[pos]);
    }
maior = numeros[0];
for (pos = 0; pos < 10; pos++){
    if (numeros[pos] > maior){
        maior = numeros[pos];
    }
}

printf("Maior valor = %d\n", maior);
    return 0;
}