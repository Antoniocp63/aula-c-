// Online C compiler to run C program online
#include <stdio.h>

int main() {
   int senha;
   printf("Informe sua senha: \n");
   scanf("%d", &senha);
   while (senha != 1234); {
       printf("Informe a senha novamente: \n");
       scanf("%d", &senha);
   }
   printf("Login completo");
    return 0;
}