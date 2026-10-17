
turma = {
    "2026001": {"nome": "Ana", "nota": 8.5},
    "2026002": {"nome": "Bruno", "nota": 6.0},
    "2026003": {"nome": "Carla", "nota": 9.2}
}

soma_notas = 0

for matricula, aluno in turma.items():
    nome = aluno["nome"]
    nota = aluno["nota"]

    if nota >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"{nome} - Nota: {nota} - Situação: {situacao}")

    soma_notas += nota

media = soma_notas / len(turma)

print(f"\nMédia geral da turma: {media:.2f}")
