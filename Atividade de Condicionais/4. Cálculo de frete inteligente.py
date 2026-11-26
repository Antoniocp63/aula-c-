
print("=== CÁLCULO DE FRETE INTELIGENTE ===")

peso = float(input("Peso da encomenda em kg: "))
distancia = float(input("Distância em km: "))
tipo = input("Tipo de entrega (normal, expressa ou urgente): ").lower()
assinante = input("É assinante? (sim/nao): ").lower()
compra = float(input("Valor da compra: R$ "))

if (peso <= 0 or distancia <= 0 or compra < 0
    or tipo not in ["normal", "expressa", "urgente"]
    or assinante not in ["sim", "nao"]):

    print("Valores inválidos!")

else:
    taxa_peso = peso * 2.50
    taxa_distancia = distancia * 0.30

    valor_base = taxa_peso + taxa_distancia

    if tipo == "normal":
        adicional_entrega = 0
    elif tipo == "expressa":
        adicional_entrega = valor_base * 0.30
    else:
        adicional_entrega = valor_base * 0.60

    adicional_peso = 80 if peso > 30 else 0
    adicional_distancia = 100 if distancia > 500 else 0

    subtotal = (
        valor_base + adicional_entrega
        + adicional_peso + adicional_distancia
    )

    desconto = 0

    if assinante == "sim":
        desconto += 15

    if compra > 1000:
        desconto += 10

    desconto = min(desconto, 20)

    frete_gratis = (
        assinante == "sim"
        and compra >= 2000
        and tipo == "normal"
        and peso <= 10
    )

    valor_desconto = subtotal * (desconto / 100)

    frete = subtotal - valor_desconto

    if frete_gratis:
        frete = 0

    print("\n=== RESULTADO DO FRETE ===")
    print(f"Taxa por peso: R$ {taxa_peso:.2f}")
    print(f"Taxa por distância: R$ {taxa_distancia:.2f}")
    print(f"Adicional de entrega: R$ {adicional_entrega:.2f}")
    print(f"Adicional por peso: R$ {adicional_peso:.2f}")
    print(f"Adicional por distância: R$ {adicional_distancia:.2f}")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Desconto aplicado: {desconto}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")

    if frete_gratis:
        print("Frete grátis concedido!")

    print(f"VALOR FINAL DO FRETE: R$ {frete:.2f}")
