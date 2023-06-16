import random
import time

def exibirTabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(linha)
import random
import time

def exibirTabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(linha)

def colocarNavio(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = 1
        return True
    else:
        return False

def atacar(tabuleiro, tabuleiro_inicial, linha, coluna):
    if tabuleiro_inicial[linha][coluna] == 'X' or tabuleiro_inicial[linha][coluna] == 1:
        return False

    if tabuleiro[linha][coluna] == 1:
        tabuleiro_inicial[linha][coluna] = 'X'
        return True
    else:
        tabuleiro_inicial[linha][coluna] = 1
        return False


print("Bem-vindo ao Batalha Naval!")

tabuleiroplayer = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

tabuleirocomputador = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

tabuleiroinicioplayer = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

tabuleiroiniciocomputador = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

for linha in range(5):
    print(tabuleiroplayer[linha])

for escolha in range(5):
    while True:
        linhaplayer = int(input("Escolha a linha em que deseja colocar essa embarcação (1 a 5): ")) - 1
        colunaplayer = int(input("Escolha a coluna em que deseja colocar essa embarcação (1 a 10): ")) - 1

        if 0 <= linhaplayer < 5 and 0 <= colunaplayer < 10:
            if colocarNavio(tabuleiroplayer, linhaplayer, colunaplayer):
                break
            else:
                print('Você já posicionou um navio nessa posição, escolha outra.')
        else:
            print('Posição inválida. Tente novamente')

    for linha in range(5):
        print(tabuleiroplayer[linha])

for escolhacomputador in range(5):
    while True:
        linhacomputador = random.randint(0, 4)
        colunacomputador = random.randint(0, 9)
        if colocarNavio(tabuleirocomputador, linhacomputador, colunacomputador):
            break

print()
time.sleep(1)
print('**** Tabuleiro do Computador ****')

for linha in range(5):
    print(tabuleiroiniciocomputador[linha])

naviocomputador = 5
navioplayer = 5

print('-' * 40)
print(f'Embarcações restantes do Computador: {naviocomputador}')

print()
time.sleep(1)
print('**** Tabuleiro do Jogador ****')

for linha in range(5):
    print(tabuleiroinicioplayer[linha])

print('-' * 40)
print(f'Embarcações restantes do Jogador: {navioplayer}')

vitoria = 0

while vitoria == 0:
    print()
    ataquePlayerLinha = int(input("Qual linha deseja atacar? (1 a 5): ")) - 1
    ataquePlayerColuna = int(input("Qual coluna deseja atacar? (1 a 10): ")) - 1
    print()

    if 0 <= ataquePlayerLinha < 5 and 0 <= ataquePlayerColuna < 10:
        if atacar(tabuleirocomputador, tabuleiroiniciocomputador, ataquePlayerLinha, ataquePlayerColuna):
            naviocomputador -= 1
            print('Você acertou o alvo!')
        else:
            print('Que pena, você errou.')
    else:
        print('Posição inválida. Seu ataque foi anulado, ataque na próxima rodada.')

    exibirTabuleiro(tabuleiroiniciocomputador)
    print(f'Embarcações restantes do Computador: {naviocomputador}')

    if naviocomputador == 0:
        print("Fim de Jogo. Parabéns, você ganhou!")
        vitoria += 1
        print("Obrigado por testar o nosso jogo de Batalha Naval!")
        print("Jogo desenvolvido por Andrei Silva, Arthur Huçulak, Gabriel Baú, Henrique Colle e Nestor")

    ataqueComputadorLinha = random.randint(0, 4)
    ataqueComputadorColuna = random.randint(0, 9)

    print()
    time.sleep(1.5)
    if atacar(tabuleiroplayer, tabuleiroinicioplayer, ataqueComputadorLinha, ataqueComputadorColuna):
        navioplayer -= 1
        print('O computador acertou o seu navio!')
    else:
        print('O computador errou.')

    exibirTabuleiro(tabuleiroinicioplayer)
    print(f'Embarcações restantes do Jogador: {navioplayer}')

    if navioplayer == 0:
        print("Fim de Jogo, o Computador ganhou!")
        vitoria += 1
        print("Obrigado por testar o nosso jogo de Batalha Naval!")
        print("Jogo desenvolvido por Andrei Silva, Arthur Huçulak, Gabriel Baú, Henrique Colle e Nestor")

def colocarNavio(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = 1
        return True
    else:
        return False

def atacar(tabuleiro, tabuleiro_inicial, linha, coluna):
    if tabuleiro_inicial[linha][coluna] == 'X' or tabuleiro_inicial[linha][coluna] == 1:
        return False

    if tabuleiro[linha][coluna] == 1:
        tabuleiro_inicial[linha][coluna] = 'X'
        return True
    else:
        tabuleiro_inicial[linha][coluna] = 1
        return False


print("Bem-vindo ao Batalha Naval! ")

tabuleiroplayer = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

tabuleirocomputador = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

tabuleiroinicioplayer = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

tabuleiroiniciocomputador = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

for linha in range(5):
    print(tabuleiroplayer[linha])

for escolha in range(5):
    while True:
        linhaplayer = int(input("Escolha a linha em que deseja colocar essa embarcação: ")) - 1
        colunaplayer = int(input("Escolha a coluna em que deseja colocar essa embarcação: ")) - 1

        if colocarNavio(tabuleiroplayer, linhaplayer, colunaplayer):
            break
        else:
            print('Você já posicionou um navio nessa posição, escolha outra.')

    for linha in range(5):
        print(tabuleiroplayer[linha])

for escolhacomputador in range(5):
    while True:
        linhacomputador = random.randint(0, 4)
        colunacomputador = random.randint(0, 9)
        if colocarNavio(tabuleirocomputador, linhacomputador, colunacomputador):
            break

print()
time.sleep(1)
print('**** Tabuleiro do Computador ****')

for linha in range(5):
    print(tabuleiroiniciocomputador[linha])

naviocomputador = 5
navioplayer = 5

print('-' * 40)
print(f'Embarcações restantes do Computador: {naviocomputador}')

print()
time.sleep(1)
print('**** Tabuleiro do Jogador ****')

for linha in range(5):
    print(tabuleiroinicioplayer[linha])

print('-' * 40)
print(f'Embarcações restantes do Jogador: {navioplayer}')

vitoria = 0

while vitoria == 0:
    print()
    ataquePlayerLinha = int(input("Qual linha deseja atacar?: ")) - 1
    ataquePlayerColuna = int(input("Qual coluna deseja atacar?: ")) - 1
    print()

    if atacar(tabuleirocomputador, tabuleiroiniciocomputador, ataquePlayerLinha, ataquePlayerColuna):
        naviocomputador -= 1
        print('Você acertou o alvo!')
    else:
        print('Que pena, você errou.')

    exibirTabuleiro(tabuleiroiniciocomputador)
    print(f'Embarcações restantes do Computador: {naviocomputador}')

    if naviocomputador == 0:
        print("Fim de Jogo. Parabéns, você ganhou!")
        vitoria += 1
        print("Obrigado por testar o nosso jogo de Batalha Naval!")
        print("Jogo desenvolvido por Andrei Silva, Arthur Huçulak, Gabriel Baú, Henrique Colle e Nestor")

    ataqueComputadorLinha = random.randint(0, 4)
    ataqueComputadorColuna = random.randint(0, 9)

    print()
    time.sleep(1.5)
    if atacar(tabuleiroplayer, tabuleiroinicioplayer, ataqueComputadorLinha, ataqueComputadorColuna):
        navioplayer -= 1
        print('O computador acertou o seu navio!')
    else:
        print('O computador errou.')

    exibirTabuleiro(tabuleiroinicioplayer)
    print(f'Embarcações restantes do Jogador: {navioplayer}')

    if navioplayer == 0:
        print("Fim de Jogo, o Computador ganhou!")
        vitoria += 1
        print("Obrigado por testar o nosso jogo de Batalha Naval!")
        print("Jogo desenvolvido por Andrei Silva, Arthur Huçulak, Gabriel Baú, Henrique Colle e Nestor")
