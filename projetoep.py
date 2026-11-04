def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])

    return posicoes

def preenche_frota (frota,nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
         frota[nome_navio] = []
        
    frota[nome_navio].append(posicoes)
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)

    for nome in frota:
        for navio in frota[nome]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro

def afundados(frota, tabuleiro):
    total = 0
    for nome in frota:
        for navio in frota[nome]:
            afundado = True
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] != "X":
                    afundado = False
                    break
            if afundado:
                total += 1
    return total

def posicao_valida(frota,linha,coluna,orientacao,tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    for posicao in posicoes:
        linha = posicao[0]
        coluna = posicao[1]
        
        if linha < 0 or linha >= 10 or coluna < 0 or coluna >= 10:
            return False
        
        for nome in frota:
            for navio in frota[nome]:
                if posicao in navio:
                    return False
    return True

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