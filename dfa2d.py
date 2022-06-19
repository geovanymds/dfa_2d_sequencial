import numpy as numpy
from scipy import stats
import robustLastSquare as fit
import time

def dfa2d(mat, grau):
    inicio = time.time()
    [l, c] = numpy.shape(mat)
    tam = numpy.minimum(l, c)
    mat = numpy.reshape(mat, (tam, tam))
    escalas = int(tam/4)
    vetoutput = numpy.zeros(shape=(escalas - 5, 2))
    #vetoutput = numpy.zeros(shape=(1, 2))
    k=0
    s = 6
    boxratio = numpy.power(2.0, 1.0 / 8.0)
    while (s < escalas + 1):
        matAtual = mat
        tamAtual = tam
        if numpy.mod(tamAtual, s) != 0:
            tamAtual = s * int(numpy.trunc(tamAtual / s))
            matAtual = mat[0:tamAtual, 0:tamAtual]
        # Passo 1 : Subdivisão da Série Temporal
        qt = int(numpy.power((tamAtual / s), 2)) #quantidade de sub-matrizes
        t = numpy.arange(s, tamAtual, s) #intervalos para o split da matriz em sub-matrizes
        aux = numpy.array(numpy.array_split(matAtual, t, axis=1))
        matAtual = numpy.reshape(aux, (qt, s, s))
        # Passo 2 : Integração e Remoção da Tendência
        vetvar = [fit.fit2D((numpy.cumsum(m).reshape(s,s)), s, grau) for m in matAtual]
        # 4.Calcula-se a função de flutuação DFA como a média das variâncias de cada intervalo:
        fs = numpy.sqrt(numpy.mean(vetvar))
        vetoutput[k, 0] = s
        vetoutput[k, 1] = fs
        # vetoutput = numpy.vstack((vetoutput, [s, fs]))
        # s = numpy.ceil(s * boxratio).astype(numpy.int)
        k = k + 1
        s = s + 1
    #vetoutput = numpy.log10(vetoutput[1::1, :])
    vetoutput = numpy.log10(vetoutput)
    x = vetoutput[:, 0]
    y = vetoutput[:, 1]
    slope, _, _, _, _ = stats.linregress(x, y)
    fim = time.time()
    print(slope)
    return (slope, fim-inicio, y.reshape(1,-1))
