#Jogo da velha
tabuleiro = [['_','_','_'],['_','_','_'],['_','_','_']]
px = 'X'
po = 'O'

def jogar():
    print('***** JOGO DA VELHA *****')
    mostrarTabuleiro()

    while True:
        inserirLinhaColuna(px)
        if ganhar():
            break
        mostrarTabuleiro()
        inserirLinhaColuna(po)
        if ganhar():
            break
        mostrarTabuleiro()


def mostrarTabuleiro():
    for l in range(0,3):
        for c in range(0,2):
            print(f'{tabuleiro[l][c]:^3}', end='|')
        print(f"{tabuleiro[l][2]:^3}", end='')
        print()


def inserirLinhaColuna(jogador):
    linha, coluna = map(int, input('\nJogador '+ jogador+' | Digite linha e coluna (1, 2 ou 3 e separe com espaço): ').split())
    print()

    tabuleiro[(linha - 1)][(coluna - 1)] = jogador

def ganhar():
    linha =ganharLinha()
    coluna = ganharColuna()
    diagonal = ganharDiagonal()
    velha = darVelha()

    if(linha == True or coluna == True or diagonal == True or velha == True):
        mostrarTabuleiro()
        return True

def ganharLinha():
    for i in range (0,3):
        if tabuleiro[i][0] == 'X' and tabuleiro[i][1] == 'X' and tabuleiro[i][2] == 'X':
            print('O jogador X é o vencedor!')
            return True

        if tabuleiro[i][0] == 'O' and tabuleiro[i][1] == 'O' and tabuleiro[i][2] == 'O':
            print('O jogador O é o vencedor!')
            return True

        else:
            return False

def ganharColuna():
    for j in range(0,3):
        if tabuleiro[0][j] == 'X' and tabuleiro[1][j] == 'X' and tabuleiro[2][j] == 'X':
            print('O jogador X é o vencedor!')
            return True

        if tabuleiro[0][j] == 'O' and tabuleiro[1][j] == 'O' and tabuleiro[2][j] == 'O':
            print('O jogador O é o vencedor!')
            return True

        else:
            return False

def ganharDiagonal():
    if tabuleiro[0][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][2] == 'X':
        print('O jogador X é o vencedor!')
        return True

    if tabuleiro[0][2] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][0] == 'X':
        print('O jogador X é o vencedor!')
        return True
    
    if tabuleiro[0][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][2] == 'O':
        print('O jogador O é o vencedor!')
        return True

    if tabuleiro[0][2] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][0] == 'O':
        print('O jogador O é o vencedor!')
        return True

    else:
        return False

def darVelha():
    if (tabuleiro[0][0] != '_' and tabuleiro[0][1] != '_'and tabuleiro[0][2] != '_'):
        if(tabuleiro[1][0] != '_' and tabuleiro[1][1] != '_' and tabuleiro[1][2] != '_'):
            if (tabuleiro[2][0] != '_' and tabuleiro[2][1] != '_' and tabuleiro[2][2] != '_'):
                if (ganharLinha() == False and ganharColuna() == False and ganharDiagonal() == False):
                    print ("Deu velha!")
                    return True
    return False

jogar()