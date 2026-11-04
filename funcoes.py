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

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ""
    texto += "   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n"
    texto += "_______________________________      _______________________________\n"

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = "  ".join(
            [str(item) for item in tabuleiro_jogador[linha]]
        )

        oponente_info = "  ".join(
            [str(info) if str(info) in "X-" else "0"
             for info in tabuleiro_oponente[linha]]
        )

        texto += f"{linha}| {jogador_info}|     {linha}| {oponente_info}|\n"

    return texto
  