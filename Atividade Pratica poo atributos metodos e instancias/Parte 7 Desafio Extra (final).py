frota = [veiculo1, veiculo2, veiculo3]

print("Todos os veículos da frota:")

for veiculo in frota:
    veiculo.exibir_dados()

print("Veículos disponíveis para aluguel:")

for veiculo in frota:
    if veiculo.disponivel:
        print(veiculo.modelo)
