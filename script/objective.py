import numpy as np

def black_box(array, scale=0.001):
    
    def f(array):
        dim = len(array)
        return np.sum(np.sin(array)) + dim
    
    return np.random.normal(loc=f(array), scale=scale)
