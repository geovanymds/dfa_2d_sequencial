import numpy as numpy
import codecs

def readInput(inputPath,delimiter):
    with codecs.open(inputPath, encoding='utf-8-sig') as f:
        x = numpy.loadtxt(f, delimiter=delimiter)
    return x
