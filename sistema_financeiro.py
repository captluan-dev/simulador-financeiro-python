def aplicar_juros_investimento(jogador):
    rendimento = jogador['investimentos'] * 0.05
    jogador['saldo'] += rendimento
    print(f'Você recebeu um rendimento de R${rendimento:.2f} dos seus investimentos. Saldo atual: R${jogador["saldo"]:.2f}.')

def aplicar_juros_divida(jogador):
    if jogador['dividas'] < 0:
        print('Você não tem dívidas para acumular juros.')
        return
    
    juros = jogador['dividas'] * 1.05
    jogador['dividas'] = juros
    print(f'As suas dívidas acumularam juros. Dívidas atuais: R${jogador["dividas"]:.2f}.')

def aplicar_inflacao(jogador):
    jogador['despesas_fixas'] *= 1.02
    print(f'Devido à inflação, suas despesas fixas aumentaram para R${jogador["despesas_fixas"]:.2f}.')