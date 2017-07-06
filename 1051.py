salario = float(input())
imposto = 0

base = salario - 2000
if salario >= 0 and salario <= 2000:
    print("Insento")
elif salario > 2000 and salario <= 3000:
    imposto = base * 0.08
    print("R$ %5.2f" % imposto)
elif salario > 3000 and salario <= 4500:
    if base > 1000:
        base = base - 1000
        imposto = base * 0.18
        base = 1000
        imposto += base * 0.08
    print("R$ %5.2f" % imposto)
else:
    '''Problema estranho de resolver ainda estou tentando'''