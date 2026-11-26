
print("=== CÁLCULO DE IMPOSTO DE RENDA ===")

salario = float(input("Digite o salário bruto: R$ "))
dependentes = int(input("Quantidade de dependentes: "))
previdencia = float(input("Valor pago em previdência: R$ "))
pensao = float(input("Valor pago em pensão alimentícia: R$ "))

if salario < 0 or dependentes < 0 or previdencia < 0 or pensao < 0:
    print("Valores inválidos!")
else:
    deducao_dependentes = dependentes * 250

    total_deducoes = (
        previdencia + pensao + deducao_dependentes
    )

    base = salario - total_deducoes

    if base < 0:
        print("Erro: as deduções são maiores que o salário bruto.")

    else:
        if base <= 2500:
            aliquota = 0
        elif base <= 3500:
            aliquota = 7.5
        elif base <= 5000:
            aliquota = 15
        elif base <= 7500:
            aliquota = 22.5
        else:
            aliquota = 27.5

        imposto = base * (aliquota / 100)
        salario_liquido = salario - total_deducoes - imposto

        print("\n=== RESULTADO ===")
        print(f"Salário bruto: R$ {salario:.2f}")
        print(f"Total de deduções: R$ {total_deducoes:.2f}")
        print(f"Base de cálculo: R$ {base:.2f}")
        print(f"Alíquota: {aliquota:.1f}%")
        print(f"Imposto: R$ {imposto:.2f}")
        print(f"Salário líquido: R$ {salario_liquido:.2f}")
