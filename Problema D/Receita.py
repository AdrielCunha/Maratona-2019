'''5
100 200
150 300
500 250
200 400
250 250
0'''

dias = []
a = 1
boloMilho = 0
boloCoco = 0
ingMilho = [200, 200, 250, 200, 4, 15, 15, 5, 0]
ingCoco = [0, 120, 360, 0, 4, 240, 100, 10, 200]
ingTotal = []
nome = ['Milho Verde', 'Óleo Vegetal', 'Açúcar', 'Fubá', 'Ovos', 'Farinha de trigo',
        'Coco ralado', 'Fermento em pó', 'Leite de coco']

while a != '0':
    a = str(input())
    dias.append(a)
for i in range(1, len(dias)):
    dias[i] = dias[i].split()

for i in range(1, len(dias) - 1):
    boloMilho += int(dias[i][0])
    boloCoco += int(dias[i][1])

for i in range(0, 9):
        ingMilho[i] *= boloMilho
        ingCoco[i] *= boloCoco
        ingTotal.append(ingMilho[i] + ingCoco[i])
        if i != 1 and i != 8 and i != 4:
            ingTotal[i] //= 1000
        if i == 1 or i == 8:
            ingTotal[i] //= 1000

for i in range(0, 9):
    if i != 1 and i != 8 and i != 4:
        print('{} {} Kg'.format(nome[i], ingTotal[i]))
    elif i == 1 or i == 8:
        print('{} {} L'.format(nome[i], ingTotal[i]))
    else:
        print(nome[i], ingTotal[i])
