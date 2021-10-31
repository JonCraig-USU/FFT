import numpy as np

def getComplex(n):
    w = [complex(np.cos(2*np.pi * i/n), np.sin(2*np.pi * i/n)) for i in range(n)]
    return w

print(getComplex(8))

def fft(p, w, n):
    return None