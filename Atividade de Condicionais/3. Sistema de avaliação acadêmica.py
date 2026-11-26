
print("=== SISTEMA DE AVALIAÇÃO ACADÊMICA ===")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

frequencia = float(input("Digite o percentual de frequência: "))
entregues = int(input("Quantidade de atividades entregues: "))
total = int(input("Quantidade total de atividades: "))

if (not 0 <= nota1 <= 10 or not 0 <= nota2 <= 10
    or not 0 <= nota3 <= 10 or not 0 <= frequencia <= 100
    or entregues < 0 or total <= 0 or entregues > total):

    print("Valores inválidos!")

else:
    media = (nota1 + nota2 + nota3) / 3
    percentual = (entregues / total) * 100

    print("\n=== RESULTADO ===")
    print(f"Média: {media:.2f}")
    print(f"Frequência: {frequencia:.2f}%")
    print(f"Atividades entregues: {percentual:.2f}%")

    if frequencia < 75:
        print("Resultado: REPROVADO POR FREQUÊNCIA")
        print("Motivo: frequência inferior a 75%.")

    elif media < 5:
        print("Resultado: REPROVADO POR NOTA")
        print("Motivo: média inferior a 5.")

    elif (media >= 9 and frequencia >= 90
          and entregues == total):
        print("Resultado: APROVADO COM EXCELÊNCIA")

    elif (media >= 7 and frequencia >= 75
          and percentual >= 70):
        print("Resultado: APROVADO")

    elif media >= 5 and media < 7:
        print("Resultado: RECUPERAÇÃO")

    else:
        print("Resultado: NÃO ATENDE AOS REQUISITOS DE APROVAÇÃO.")

    print("\n=== REQUISITO QUE IMPEDE UMA CLASSIFICAÇÃO SUPERIOR ===")

    if media < 9:
        print("A média é inferior a 9.")
    elif frequencia < 90:
        print("A frequência é inferior a 90%.")
    elif entregues < total:
        print("Existem atividades não entregues.")
    else:
        print("Todos os requisitos foram atendidos.")
