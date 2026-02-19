import utils
import jogador
import config
import eventos
import sistema_financeiro

utils.long_lines()
print('                   SIMULADOR FINANCEIRO                   ')
utils.long_lines()
print('Pronto para viver uma vida financeira cheia de decisões?\n')
utils.pause()
utils.clear()

print('Vamos começar criando o seu jogador!')
usuario = jogador.criar_jogador()
utils.clear()

utils.long_lines()
print(f'Bem-vindo, {usuario["nome"]}! Sua jornada financeira começa agora.')
print(f'Você tem um saldo inicial de R${usuario["saldo"]:.2f} e um salário mensal de R${usuario["salario"]:.2f}.')
utils.long_lines()
utils.pause()
utils.clear()

for mes in config.meses:
    utils.short_lines()
    print(f'           {mes}              ')
    utils.short_lines()
    jogador.receber_salario(usuario)
    jogador.pagar_despesas(usuario)

    print('\nO que você gostaria de fazer?')
    print('1 - Investir')
    print('2 - Pegar um empréstimo')
    print('3 - Pagar dívidas')
    print('4 - Passar para o próximo mês')

    escolha = input('Escolha: ')

    while escolha not in ['1', '2', '3', '4']:
        print('Opção inválida. Por favor, escolha uma opção válida.')
        escolha = input('Escolha: ')

    if escolha == '1':
        valor = float(input('Quanto você quer investir? R$'))
        jogador.investir(usuario, valor)
    
    elif escolha == '2':
        valor = float(input('Quanto você quer pegar de empréstimo? R$'))
        jogador.pegar_emprestimo(usuario, valor)

    elif escolha == '3':
        valor = float(input('Quanto você quer pagar da sua dívida? R$'))
        jogador.pagar_divida(usuario, valor)

    elif escolha == '4':
        print('Indo para o próximo mês...')

    eventos.evento_aleatorio(usuario)
    utils.pause()
    utils.clear()

    sistema_financeiro.aplicar_juros_investimento(usuario)
    sistema_financeiro.aplicar_juros_divida(usuario)
    sistema_financeiro.aplicar_inflacao(usuario)
    utils.pause()

    print('\nResumo do mês:')
    print(f'Saldo: R${usuario["saldo"]:.2f}')
    print(f'Investimentos: R${usuario["investimentos"]:.2f}')
    print(f'Dívidas: R${usuario["dividas"]:.2f}')
    print(f'Nível de estresse: {usuario["estresse"]}')
    utils.pause()
    utils.clear()

# Fim do ano - Avaliação final

utils.clear()
pontuacao = usuario['saldo'] + usuario['investimentos'] * 1.2 - usuario['dividas'] * 1.5 - (usuario['estresse'] * 100)
    
resultado = utils.avaliar_resultado(pontuacao)

utils.long_lines()
print('                   RESULTADO FINAL                   ')
print('Fim de ano! Vamos ver como você se saiu financeiramente.')
print(f'Saldo final: R${usuario["saldo"]:.2f}')
print(f'Investimentos finais: R${usuario["investimentos"]:.2f}')
print(f'Dívidas: R${usuario["dividas"]:.2f}')
print(f'Nível de estresse: {usuario["estresse"]}')
print(f'Pontuação final: {pontuacao:.2f}')
print(f'Classificação: {resultado}')

if pontuacao >= 20000:
    print('Parabéns! Você é um Magnata Financeiro! Sua habilidade de investir e controlar suas finanças é impressionante.')

elif pontuacao < 0:
    print('O ano foi difícil. Talvez seja hora de reavaliar suas estratégias financeiras.')
utils.long_lines()