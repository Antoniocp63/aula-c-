
produto = {
    "nome": "Notebook",
    "preco": 4500.00,
    "estoque": 12
}

chave = input("Digite a informação desejada: ")

valor = produto.get(chave)

if valor is not None:
    print(valor)
else:
    print("Informação não encontrada.")
