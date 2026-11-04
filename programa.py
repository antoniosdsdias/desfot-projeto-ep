from funcoes import (
    posicao_valida,
    preenche_frota,
    posiciona_frota,
    monta_tabuleiros,
    faz_jogada,
    afundados
)


# Posicionamento dos navios do jogador
frota = {}

embarcacoes = [
    ["porta-aviões", 1, 4],
    ["navio-tanque", 2, 3],
    ["contratorpedeiro", 3, 2],
    ["submarino", 4, 1]
]

for nome, quantidade, tamanho in embarcacoes:
    for i in range(quantidade):
        valida = False

        while not valida:
            print(
                f"Insira as informações referentes ao navio {nome} "
                f"que possui tamanho {tamanho}"
            )

            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome == "submarino":
                orientacao = "vertical"
            else:
                escolha = int(
                    input("Orientação: [1] Vertical [2] Horizontal ")
                )

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


# Posicionamento fixo do oponente
frota_oponente = {
    "porta-aviões": [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    "navio-tanque": [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    "contratorpedeiro": [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    "submarino": [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

total_navios = 0

for nome in frota_oponente:
    total_navios += len(frota_oponente[nome])

jogadas = []
jogando = True


# Ataques do jogador
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    nova_posicao = False

    while not nova_posicao:
        linha = int(input("Jogador, qual linha deseja atacar? "))

        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))

        coluna = int(input("Jogador, qual coluna deseja atacar? "))

        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))

        if [linha, coluna] in jogadas:
            print(
                f"A posição linha {linha} e coluna {coluna} "
                "já foi informada anteriormente!"
            )
        else:
            nova_posicao = True

    jogadas.append([linha, coluna])

    tabuleiro_oponente = faz_jogada(
        tabuleiro_oponente, linha, coluna
    )

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False