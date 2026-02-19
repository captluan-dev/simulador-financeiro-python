import os

def long_lines():
    print('=' * 60)

def short_lines():
    print('=' * 30)

def pause():
    input('Pressione ENTER para continuar...')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def avaliar_resultado(pontuacao):
    if pontuacao >= 20000:
        return 'Magnata Financeiro'
    
    elif pontuacao >= 10000:
        return 'Investidor Estratégico'
    
    elif pontuacao >= 5000:
        return 'Organizado Financeiramente'
    
    elif pontuacao >= 0:
        return 'Sobreviveu ao Ano'
    
    else:
        return 'Endividado e Estressado'