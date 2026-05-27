#include <stdio.h>

int main() {
    float notas[8];
    float frequencia;
    int i;

    int aprovados = 0;
    int reprovados = 0;

    float maiorNota = 0;

    for(i = 0; i < 8; i++) {

        printf("Participante %d\n", i + 1);

        printf("Digite a nota: ");
        scanf("%f", &notas[i]);

        printf("Digite a frequencia: ");
        scanf("%f", &frequencia);

        if(notas[i] >= 7 && frequencia >= 75) {
            printf("APROVADO\n");
            aprovados++;
        } else {
            printf("REPROVADO\n");
            reprovados++;
        }

        if(i == 0 || notas[i] > maiorNota) {
            maiorNota = notas[i];
        }

        printf("\n");
    }

    printf("Quantidade de aprovados: %d\n", aprovados);
    printf("Quantidade de reprovados: %d\n", reprovados);
    printf("Maior nota registrada: %.2f\n", maiorNota);

    return 0;
}