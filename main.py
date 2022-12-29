from random import randint
itens = ("FOGO", "ÁGUA" ,"PLANTA")
computador = randint(0, 2)
print("=-_-=" *9)
print('''Suas opções são:
[0] FOGO
[1] ÁGUA
[2] PLANTA''')
jogador = int(input("Qual é a sua jogada? -> "))
print("=-_-=" *9)
print("jogador jogou {}".format(itens[jogador]))
print("computador jogou {}".format(itens[computador]))
print("=-_-=" *9)
if jogador == computador:
    print('empatou!')
elif jogador == 0 and computador == 1:
    print('você perdeu...')
elif jogador == 1 and computador == 0:
    print('você venceu!')
elif jogador == 2 and computador == 1:
    print('você venceu!')
elif jogador == 1 and computador == 2:
    print('você perdeu...')
elif jogador == 2 and computador == 0:
    print('você perdeu...')
else:
    print('você venceu!')
