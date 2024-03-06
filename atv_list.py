# 1) observe o trecho de código a baixo:

indice = 13
soma = 0
k = 0

while k < indice:
    k = k+1
    soma = soma + k

print(soma)

# Ao final do processo, qual será o valor da variável soma? Resposta e 91

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

fibonacci = []
infonum = int(input('Informe um numero:'))
soma = 0
i = 0

while i < infonum:
    fibonacci.append(soma)
    i = i+1
    soma = soma + k

if infonum in fibonacci:
    print(f' O numero {infonum} pertence a sequência de Fibonacci')
else:
    print(f' O numero {infonum} não pertence a sequência de Fibonacci')

"""
3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, ___ 2

b) 2, 4, 8, 16, 32, 64, ____ 128

c) 0, 1, 4, 9, 16, 25, 36, ____49

d) 4, 16, 36, 64, ____100

e) 1, 1, 2, 3, 5, 8, ____13

f) 2,10, 12, 16, 17, 18, 19, ____20

"""

"""
4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente.
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes
quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor
controla cada lâmpada?

ligo 2 interruptores e visito uma das salas;
caso 1:
    se a luz da sala estiver ligada a 50% de chance que um dos interruptores acionados seja o da sala;
    volto a sala do interruoitores;
    desligo um dos interrupitores que foram ativados;
    visito outra sala;
    se a luz da sala estive ligada a 100% que o interropitor ativo e o da sala;
    se a luz não estiver ligada confiro a temperatura da lampada;
    se ainda estiver quente quer dizer que o interrupitor que foi desligado e o da sala;
    se não aquela e a sala do interrupitor que nao foi ativado;
caso 2:
    se a luz estiver desligada a 100% de certeza que o interropitor que não foi ativado e o da sala visitada;
    volto a sala do interruoitores;
    desligo um dos interruptores ativados;
    visito outra sala;
    se a luz estiver liga o interruptor que esta ativo eo da sala,
    se a luz não estiver ligada o interruptor que foi desativado pertence aquela sala
"""

"""
5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""

texto = str(input('Escreva uma frase:'))
novtex = ''

for letra in texto:
    temp = letra + novtex
    novtex = temp

print(novtex)