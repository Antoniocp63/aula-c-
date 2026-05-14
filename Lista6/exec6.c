// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int numeros [10];
    int pos, valor, encontrado = 0;
    
    for (pos = 0; pos < 10; pos++){
        printf("Digite o número da posição %d: ", pos);
        scanf("%d", &numeros[pos]);
    }
    printf("Digite o valor a ser buscado: ");
    scanf("%d", &valor);
    for (pos = 0; pos < 10; pos++){
        if (numeros[pos] == valor){
            encontrado = 1;
        }
    }
    if (encontrado) {
        printf("Valor encontrado!\n");
    } else {
        printf("Valor nao encontrado!\n");
    }
    

    return 0;
}