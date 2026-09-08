saldo = 0
tentativas = 3
senha_correta = "1234"

autenticado = False

while tentativas > 0:
    senha = input("Digite sua senha: ")

    if senha == senha_correta:
        autenticado = True
        print("Login realizado com sucesso!")
        break
    else:
        tentativas -= 1
        print("Senha incorreta!")
        print("Tentativas restantes:", tentativas)

if autenticado:
    depositos = 0
    saques = 0
    total_depositado = 0
    total_sacado = 0

    while True:
        print("\n CAIXA ELETRÔNICO ")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Exibir quantidade de operações")
        print("5 - Encerrar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Saldo atual: R$ {saldo:.2f}")

        elif opcao == "2":
            valor = float(input("Digite o valor do depósito: "))

            if valor <= 0:
                print("O depósito deve ser maior que zero.")
            else:
                saldo += valor
                depositos += 1
                total_depositado += valor
                print("Depósito realizado com sucesso.")

        elif opcao == "3":
            valor = float(input("Digite o valor do saque: "))

            if valor <= 0:
                print("O saque deve ser maior que zero.")
            elif valor > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= valor
                saques += 1
                total_sacado += valor
                print("Saque realizado com sucesso.")

        elif opcao == "4":
            print("Quantidade de depósitos:", depositos)
            print("Quantidade de saques:", saques)
            print("Total de operações:", depositos + saques)

        elif opcao == "5":
            print("\n RELATÓRIO FINAL ")
            print(f"Saldo final: R$ {saldo:.2f}")
            print("Quantidade de depósitos:", depositos)
            print("Quantidade de saques:", saques)
            print(f"Total depositado: R$ {total_depositado:.2f}")
            print(f"Total sacado: R$ {total_sacado:.2f}")
            print("Total de operações:", depositos + saques)
            print("Caixa eletrônico encerrado.")
            break

        else:
            print("Opção inválida.")

else:
    print("Número máximo de tentativas atingido.")