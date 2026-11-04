from funcoes import posicao_valida, preenche_frota
frota = {}
embarcacoes = [
    ["porta-aviões", 1, 4],
    ["navio-tanque", 2, 3],
    ["contratorpedeiro", 3, 2],
    ["submarino", 4, 1]
]

for nome, quantidade, tamanho in embarcacoes:
    for i in range(quantidade):
        print(
            f"Insira as informações referentes ao navio {nome} "
            f"que possui tamanho {tamanho}"
        )

        valida = False

        while not valida:
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome == "submarino":
                orientacao = "vertical"
            else:
                escolha = int(input("Orientação (1: vertical, 2: horizontal): "))

                if escolha == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            valida = posicao_valida(
                frota, linha, coluna, orientacao, tamanho
            )

            if not valida:
                print("Esta posição não está válida!")

        frota = preenche_frota(
            frota, nome, linha, coluna, orientacao, tamanho
        )

print(frota)