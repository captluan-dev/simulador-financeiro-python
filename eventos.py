import random

def evento_aleatorio(jogador):
    evento = random.randint(1, 5)

    if evento == 1:
        jogador['saldo'] -= 800
        print('Seu carro quebrou! Você teve que gastar R$800 para consertá-lo. Saldo atual: R${:.2f}.'.format(jogador['saldo']))
    
    elif evento == 2:
        jogador['saldo'] -= 1200
        print('Você teve uma emergência médica! Gastou R$1200. Saldo atual: R${:.2f}.'.format(jogador['saldo']))

    elif evento == 3:
        jogador['saldo'] += 1000
        print('Você recebeu uma promoção no trabalho! Saldo atual: R${:.2f}.'.format(jogador['saldo']))

    elif evento == 4:
        jogador['saldo'] += 500
        print('Você ganhou um prêmio em um sorteio! Saldo atual: R${:.2f}.'.format(jogador['saldo']))

    elif evento == 5:
        if jogador['investimentos'] > 0:
            perda = jogador['investimentos'] * 0.5
            jogador['investimentos'] -= perda
            print('O mercado financeiro caiu! Você perdeu R${:.2f} dos seus investimentos. Investimentos atuais: R${:.2f}.'.format(perda, jogador['investimentos']))
        else:
            print('O mercado financeiro caiu, mas você não tinha investimentos para perder.')