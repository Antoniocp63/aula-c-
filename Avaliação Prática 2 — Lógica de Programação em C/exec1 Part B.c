#include <stdio.h>

int main() {
    int quantidades[8];
    int essencial;
    int i;

    int urgente = 0;
    int estoqueOk = 0;

    int menorQuantidade = 0;

    for(i = 0; i < 8; i++) {

        printf("Produto %d\n", i + 1);

        printf("Digite a quantidade em estoque: ");
        scanf("%d", &quantidades[i]);

        printf("Produto essencial? (1 = sim / 0 = nao): ");
        scanf("%d", &essencial);

        if(quantidades[i] < 10 && essencial == 1) {
            printf("REPOSICAO URGENTE\n");
            urgente++;
        } else {
            printf("ESTOQUE OK\n");
            estoqueOk++;
        }

        if(i == 0 || quantidades[i] < menorQuantidade) {
            menorQuantidade = quantidades[i];
        }

        printf("\n");
    }

    // =)
    printf("Quantidade de produtos com reposicao urgente: %d\n", urgente);
    printf("Quantidade de produtos com estoque ok: %d\n", estoqueOk);
    printf("Menor quantidade registrada: %d\n", menorQuantidade);

    return 0;
}