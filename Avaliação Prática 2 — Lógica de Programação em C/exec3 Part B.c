#include <stdio.h>

int main() {
    float consumos[7];
    int horarioPico;
    int i;

    int altoCusto = 0;
    int custoNormal = 0;

    float soma = 0;
    float media;

    for(i = 0; i < 7; i++) {

        printf("Equipamento %d\n", i + 1);

        printf("Digite o consumo (kWh): ");
        scanf("%f", &consumos[i]);

        printf("Esta em horario de pico? (1 = sim / 0 = nao): ");
        scanf("%d", &horarioPico);

        soma += consumos[i];

        if(consumos[i] > 100 && horarioPico == 1) {
            printf("ALTO CUSTO\n");
            altoCusto++;
        } else {
            printf("CUSTO NORMAL\n");
            custoNormal++;
        }

        printf("\n");
    }

    media = soma / 7;

    printf("Quantidade de equipamentos com alto custo: %d\n", altoCusto);
    printf("Quantidade de equipamentos com custo normal: %d\n", custoNormal);
    printf("Consumo medio dos equipamentos: %.2f kWh\n", media);

    return 0;
}