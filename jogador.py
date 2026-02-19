def criar_jogador():
    nome = input('Digite o nome do jogador: ')

    jogador = {
        'nome': nome,
        'saldo': 3000.0,
        'salario': 2500.0,
        'despesas_fixas': 1800.0,
        'dividas': 0,
        'investimentos': 0,
        'estresse': 0
    }

    return jogador

def receber_salario(jogador):
    jogador['saldo'] += jogador['salario']
    print(f'Você recebeu seu salário de R${jogador["salario"]:.2f}.')

def pagar_despesas(jogador):
    jogador['saldo'] -= jogador['despesas_fixas']
    print(f'Você pagou suas despesas fixas de R${jogador["despesas_fixas"]:.2f}.\nSaldo atual: R${jogador["saldo"]:.2f}.')

def investir(jogador, valor):
    if valor > jogador['saldo']:
        print('Saldo insuficiente para investir.')
        return

    jogador['saldo'] -= valor
    jogador['investimentos'] += valor
    print(f'Você investiu R${valor:.2f}.\nSaldo atual: R${jogador["saldo"]:.2f}.\nInvestimentos totais: R${jogador["investimentos"]:.2f}.')

def pegar_emprestimo(jogador, valor):
    jogador['saldo'] += valor
    jogador['dividas'] += valor
    jogador['estresse'] += 10
    print(f'Você pegou um empréstimo de R${valor:.2f}. Saldo atual: R${jogador["saldo"]:.2f}. Dívidas totais: R${jogador["dividas"]:.2f}. Nível de estresse: {jogador["estresse"]}.')

def pagar_divida(jogador, valor):
    if valor > jogador['saldo']:
        print('Saldo insuficiente para pagar a dívida.')
        return

    jogador['saldo'] -= valor
    jogador['dividas'] -= valor
    jogador['estresse'] = max(0, jogador['estresse'] - 5)
    print(f'Você pagou R${valor:.2f} da sua dívida. Saldo atual: R${jogador["saldo"]:.2f}. Dívidas restantes: R${jogador["dividas"]:.2f}. Nível de estresse: {jogador["estresse"]}.')

def atualizar_estresse(jogador, valor):
    jogador['estresse'] += valor
    print(f'Seu nível de estresse aumentou em {valor}. Nível atual: {jogador["estresse"]}.')