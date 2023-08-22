"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala que
frequentam cada uma das atividades;
"""

__version__ = "0.1.0"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles),
    ("Musica", aula_musica),
    ("Dança", aula_danca), ]

for nome_ativ, atividade in atividades:
    ativ_sala1 = []
    ativ_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            ativ_sala1.append(aluno)
        elif aluno in sala2:
            ativ_sala2.append(aluno)

    print(f"Atividade {nome_ativ} sala 1 ", ativ_sala1)
    print(f"Atividade {nome_ativ} sala 2 ", ativ_sala2)
    print()
    print("#" * 5)
