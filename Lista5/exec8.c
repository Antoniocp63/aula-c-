#include <stdio.h>

int main() {

    float orcamento, produto, total = 0;
    int quantidadeProdutos = 0;

    printf("Digite o orçamento: ");
    scanf("%f", &orcamento);

    while (total <= orcamento) {

        printf("Digite o valor do produto: ");
        scanf("%f", &produto);

        if (produto <= 0) {
            printf("VALOR INVALIDO\n");
        } else {

            total += produto;
            quantidadeProdutos++;

            if (total > orcamento) {
                printf("ORCAMENTO ULTRAPASSADO\n");
                break;
            }
        }
    }

    printf("\nTotal da compra: %.2f\n", total);
    printf("Produtos validos: %d\n", quantidadeProdutos);

    return 0;
}