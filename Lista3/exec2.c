#include <stdio.h>

int main() {
    int tipoUsuario, horario, autorizacao;

    printf("Digite o tipo de usuario (1-aluno, 2-professor): ");
    scanf("%d", &tipoUsuario);

    printf("Digite o horario atual: ");
    scanf("%d", &horario);

    printf("Digite a autorizacao especial (1/0): ");
    scanf("%d", &autorizacao);

    if (tipoUsuario == 2) {
        printf("ENTRADA PERMITIDA\n");
    }
    else if (tipoUsuario == 1) {
        if (horario >= 8 && horario <= 18) {
            printf("ENTRADA PERMITIDA\n");
        }
        else {
            if (autorizacao == 1) {
                printf("ENTRADA PERMITIDA\n");
            }
            else {
                printf("ENTRADA NEGADA\n");
            }
        }
    }
    else {
        printf("ENTRADA NEGADA\n");
    }

    return 0;
}