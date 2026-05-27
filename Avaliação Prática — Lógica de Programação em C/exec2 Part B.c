#include <stdio.h>

int main() {
    float vendas[10];
    int vendaEspecial;
    int i;

    float totalVendido = 0;
    int destaque = 0;
    int comum = 0;

    for(i = 0; i < 10; i++) {

        printf("Venda %d\n", i + 1);

        printf("Digite o valor da venda: ");
        scanf("%f", &vendas[i]);

        printf("Venda especial? (1 = sim / 0 = nao): ");
        scanf("%d", &vendaEspecial);

        totalVendido += vendas[i];

        if(vendas[i] >= 100 || vendaEspecial == 1) {
            printf("VENDA COM DESTAQUE\n");
            destaque++;
        } else {
            printf("VENDA COMUM\n");
            comum++;
        }

        printf("\n");
    }

    printf("Total vendido: R$ %.2f\n", totalVendido);
    printf("Quantidade de vendas com destaque: %d\n", destaque);
    printf("Quantidade de vendas comuns: %d\n", comum);

    return 0;
}