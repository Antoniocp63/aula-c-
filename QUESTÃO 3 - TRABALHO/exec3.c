#include <stdio.h>

int main() {
    int idades[10];
    int autorizacao;

    int i;

    int liberados = 0;
    int negados = 0;

    int maiorIdade = 0;

    int somaIdades = 0;
    float media;

    for(i = 0; i < 10; i++) {

        printf("Participante %d\n", i + 1);

        printf("Digite a idade: ");
        scanf("%d", &idades[i]);

        printf("Possui autorizacao? (1 = sim, 0 = nao): ");
        scanf("%d", &autorizacao);

        somaIdades += idades[i];

        if(idades[i] > maiorIdade) {
            maiorIdade = idades[i];
        }

        if(idades[i] >= 18 || autorizacao == 1) {
            printf("ENTRADA LIBERADA\n\n");
            liberados++;
        } else {
            printf("ENTRADA NEGADA\n\n");
            negados++;
        }
    }

    media = somaIdades / 10.0;

    printf("\n===== RESULTADOS =====\n");
    printf("Quantidade de entradas liberadas: %d\n", liberados);
    printf("Quantidade de entradas negadas: %d\n", negados);
    printf("Maior idade registrada: %d\n", maiorIdade);
    printf("Media das idades: %.2f\n", media);

    return 0;
}