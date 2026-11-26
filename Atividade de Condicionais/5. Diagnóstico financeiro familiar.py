
print("=== DIAGNÓSTICO FINANCEIRO FAMILIAR ===")

renda = float(input("Renda mensal: R$ "))

moradia = float(input("Gastos com moradia: R$ "))
alimentacao = float(input("Gastos com alimentação: R$ "))
transporte = float(input("Gastos com transporte: R$ "))
saude = float(input("Gastos com saúde: R$ "))
educacao = float(input("Gastos com educação: R$ "))
lazer = float(input("Gastos com lazer: R$ "))
dividas = float(input("Gastos com dívidas: R$ "))

despesas = [
    moradia, alimentacao, transporte,
    saude, educacao, lazer, dividas
]

if renda <= 0 or any(valor < 0 for valor in despesas):
    print("Valores inválidos!")

else:
    total = sum(despesas)

    saldo = renda - total

    comprometimento = (total / renda) * 100

    percentual_dividas = (dividas / renda) * 100

    print("\n=== RESULTADO FINANCEIRO ===")
    print(f"Total de despesas: R$ {total:.2f}")
    print(f"Saldo mensal: R$ {saldo:.2f}")
    print(f"Comprometimento da renda: {comprometimento:.2f}%")
    print(f"Percentual gasto com dívidas: {percentual_dividas:.2f}%")

    if saldo < -(renda * 0.20):
        print("\nSituação: INSOLVÊNCIA")
        print("Recomendação: reduza gastos imediatamente,")
        print("renegocie dívidas e priorize despesas essenciais.")

    elif comprometimento > 85 or percentual_dividas > 35:
        print("\nSituação: CRÍTICA")
        print("Recomendação: corte gastos não essenciais,")
        print("evite novas dívidas e procure renegociar as atuais.")

    elif comprometimento > 70:
        print("\nSituação: ATENÇÃO")
        print("Recomendação: revise seu orçamento,")
        print("reduza gastos e procure aumentar sua reserva financeira.")

    elif comprometimento <= 70 and percentual_dividas <= 20:
        print("\nSituação: SAUDÁVEL")
        print("Recomendação: mantenha o controle financeiro,")
        print("evite endividamento e continue poupando.")

    else:
        print("\nSituação: ATENÇÃO")
        print("Recomendação: monitore suas despesas e reduza dívidas.")
