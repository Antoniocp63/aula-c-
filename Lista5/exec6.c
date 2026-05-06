#include <stdio.h>

int main() {
    int prioridade, continuar;
    int baixa = 0, media = 0, alta = 0;
    
    do {
        printf("Digite a prioridade (1-Baixa, 2-Media, 3-Alta): ");
        scanf("%d", &prioridade);
        
        if (prioridade == 1) {
            baixa++;
        } else if (prioridade == 2) {
            media++;
        } else if (prioridade == 3) {
            alta++;
        } else {
            printf("PRIORIDADE INVALIDA\n");
        }
        
        printf("Deseja continuar? (1-Sim / 0-Nao): ");
        scanf("%d", &continuar);
        
    } while (continuar == 1);
    
    printf("Baixa: %d\n", baixa);
    printf("Media: %d\n", media);
    printf("Alta: %d\n", alta);

    return 0;
}