#include <stdio.h>

int main() {

    float temperatura;
    int leiturasSeguras = 0;
    int leiturasRisco = 0;

    // Repetição para ler 12 temperaturas
    for (int contador = 1; contador <= 12; contador++) {

        printf("Digite a %dª temperatura: ", contador);
        scanf("%f", &temperatura);

        if (temperatura <= 75) {
            leiturasSeguras++;
        } else {
            leiturasRisco++;
        }
    }

    // Mostra o resultado final
    printf("\nResultado das leituras:\n");
    printf("Leituras seguras: %d\n", leiturasSeguras);
    printf("Leituras de risco: %d\n", leiturasRisco);

    return 0;
}