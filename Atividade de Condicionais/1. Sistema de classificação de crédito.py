
print("=== SISTEMA DE CLASSIFICAÇÃO DE CRÉDITO ===")

idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário mensal: R$ "))
divida = float(input("Digite o valor da dívida atual: R$ "))
tempo = int(input("Digite seu tempo de emprego em meses: "))
valor = float(input("Digite o valor solicitado: R$ "))
parcelas = int(input("Digite o número de parcelas: "))

if salario <= 0 or parcelas <= 0 or divida < 0 or valor <= 0:
    print("Valores inválidos!")
else:
    comprometimento = (divida / salario) * 100
    parcela = valor / parcelas
    novo_comprometimento = ((divida + parcela) / salario) * 100

    print("\n=== RESULTADO DA ANÁLISE ===")
    print(f"Valor da parcela: R$ {parcela:.2f}")
    print(f"Comprometimento atual: {comprometimento:.2f}%")
    print(f"Novo comprometimento: {novo_comprometimento:.2f}%")

    if (21 <= idade <= 65 and salario >= 2500
        and tempo >= 12 and comprometimento <= 30
        and parcela <= salario * 0.25):

        print("Resultado: APROVADA")

    elif (21 <= idade <= 65 and salario >= 2500
          and tempo >= 6 and novo_comprometimento <= 50):

        print("Resultado: APROVADA COM RESTRIÇÕES")

    else:
        print("Resultado: REPROVADA")

        if idade < 21 or idade > 65:
            print("Motivo: idade fora do limite permitido.")
        elif salario < 2500:
            print("Motivo: salário inferior a R$ 2.500.")
        elif tempo < 6:
            print("Motivo: tempo de emprego inferior a 6 meses.")
        elif novo_comprometimento > 50:
            print("Motivo: comprometimento acima de 50%.")
        elif comprometimento > 30:
            print("Motivo: dívida atual acima de 30% do salário.")
        elif parcela > salario * 0.25:
            print("Motivo: parcela acima de 25% do salário.")
