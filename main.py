import numpy as numpy
import codecs
import os
import dfa2d as dfa
from pylab import *
import utils as utils
from scipy import misc
import pandas as pd

def main(dirEntrada, dirSaida, delimiter, arqSaida):
    arqs = os.listdir(dirEntrada)
    arqs = sorted(arqs, key=lambda x: int((x.split('_')[1].split('.')[0])))
    for file in arqs:
        if file.endswith('.txt'):
            print(file)
            m = utils.readInput(dirEntrada + file,delimiter)
            alfa, tempo, F = dfa.dfa2d(m, 1)
            dt = numpy.dtype(str, 10)
            b = numpy.array([alfa, tempo], dtype=dt)
            b = numpy.reshape(b, newshape=(1, 2))
            with open(dirSaida + arqSaida, 'ab') as f:
                numpy.savetxt(f, b, fmt='%10s')

main("./data/input/mixture/","./data/output/mixture/"," ","results_mixture.txt")


