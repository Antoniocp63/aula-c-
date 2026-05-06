// Online C compiler to run C program online
#include <stdio.h>

int main() {
    float meta, valorMes, total = 0;
    int mesesValidos = 0;
    
    printf("Digite a meta da economia");
    scanf("%f", &meta);
    
    // implemente aqui um WHILE
    // Enquanto total < meta:
    // Leia valorMes.
    // Se valorMes > 0, some ao total e incremente mesesValidos.
    // Senao, exiba: VALOR DESCONSIDERADO.
    
    
    printf("Total economizado: %.2f", total);
    printf("Meses validos: %d", mesesValidos);

    return 0;
}