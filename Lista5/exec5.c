#include <stdio.h>

int main() {
    int codigo;
    
    printf("Digite o codigo de acesso: ");
    scanf("%d", &codigo);
    
    while (codigo != 4321) {
        printf("CODIGO INCORRETO\n");
        printf("Digite o codigo de acesso: ");
        scanf("%d", &codigo);
    }
    
    printf("ACESSO LIBERADO\n");

    return 0;
}