"""Dado um estacionamento cheio com um espaço vazio!
Temos um estado unicial com o estacionamento cheio e o estado final. Cada etapa nós podemos apenas
mover um carro para fora do seu local para o local vazio.
O objetivo é descobrir o mínimo de movimentos necessários para reorganizar o estacionamento,
do estado inicial para o estado final.

Exemplo:
inicio: [1, 2, 3, 0, 4]
final:   [0, 3, 2, 1, 4]
passos =  4
Sequência:
0 2 3 1 4
2 0 3 1 4
2 3 0 1 4
0 3 2 1 4 """


def garage(inicio, final):
    inicio = inicio[::]
    seq = []
    passos = 0
    while inicio != final:
        zero = inicio.index(0)
        if zero != final.index(0):
            car_to_move = final[zero]
            pos = inicio.index(car_to_move)
            inicio[zero], inicio[pos] = inicio[pos], inicio[zero]
        else:
            for i in range(len(inicio)):
                if inicio[i] != final[i]:
                    inicio[zero], inicio[i] = inicio[i], inicio[0]
                    break
        seq.append(inicio[::])
        passos += 1
    return passos, seq


inicio = [2, 3, 1, 4, 5, 0]
fim = [0, 1, 2, 3, 4, 5]

teste = garage(inicio, fim)
print(teste)
