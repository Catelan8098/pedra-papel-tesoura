# ==============================================================================
# AVISO: Por favor, respeite o trabalho investido na criação deste
# código e evite copiá-lo ou utilizá-lo sem permissão. ass: Luchas.
# ==============================================================================
#   ▂▃▅▆▇█ K █ a █ n █ f █ e █ m █   █ S █ t █ u █ d █ i █ o █ s █▇▆▅▃▂
import random
while True:	
    rps = input('Bem vindo ao Pedra, Papel e tesoura em Python!  Regras:rules Sobre:info Jogar:play Sair:esc.   ')
    if rps == 'play':
        g = input("Pedra papel tesoura!:")
        y = 'Você ganhou!'
        l = 'Você perdeu...'
        t = 'Empate!'
        r = random.choice(['tesoura', 'pedra', 'papel'])
        print (f"O computador escolheu: {r}")
        if g == r:
            print(t)
        elif r == 'pedra' and g == 'papel':
            print(y)
        elif r == 'papel' and g == 'pedra':
            print(l)
        elif r == 'papel' and g == 'tesoura':
            print(y)
        elif r == 'tesoura' and g == 'papel':	
            print(l)
        elif r == 'tesoura' and g == 'pedra':	
            print(y)
        elif r == 'pedra' and g == 'tesoura':
            print(l)    			    
    elif rps == 'rules':
        r = input('Para jogar, basta escrever: pedra, papel ou tesoura que o computador ira competir com você.   "v" para voltar "esc" para sair'   )
        if r == 'esc':
            break
    elif rps == 'info':
       i = input("Criado por: Luchas em outubro de 2023. Versão: 2.1.3. Aperte 'v' para voltar e 'esc' para sair.   ")
       if i == 'esc':
           break
    elif rps == 'esc':
        break
