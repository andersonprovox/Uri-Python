'''Entrada: um número positivo inteiro
    Saída: imprimir conforme o exemplo:
        1 2 3 PUM
        5 6 7 PUM (e por aí vai)
    Processamento: o numero de entrada é o total de linhas de saída
                    terá um acumulador que vai somar os numeros que vão aparecer sempre em uma
                    sequencia em que o 4º numero da linha escrever PUM, mas o acumulardor continuará
                    contando.'''

n = int(input())
i = 0
y = 0
a = 0
b = 0
c = 0
cum = 0
while i < n:
    #O acumulador receberá  + 4 abaixo e o a + 1
    a = cum
    a += 1
    b = a + 1
    c = b + 1
    pum = "PUM"
    cum += 4
    i += 1
    print("%d %d %d %s" % (a, b, c, pum))