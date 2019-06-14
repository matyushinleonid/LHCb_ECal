import numpy as np
from scipy.special import gammainc

def get_borders(y_middle=10, x_middle=16, a_middle=0.01, y_inner=6, x_inner=8, a_inner=0.01):
    x = np.linspace(1, x_middle, x_middle)
    y = y_middle * gammainc(a_middle, x * 0.1)
    y = np.rint(y)

    # ECAL outer borders
    y_outer = 26
    x_outer = 32
    s_outer = (y_outer, x_outer)
    
    arr = np.ones(s_outer)
    arr = arr.astype(int)

    for n in range(0, x_middle):
        arr[int((y_outer - 1) - y[n]), int(x[n] + x_middle - 1)] = 2
        
    arr = arr.transpose()
    
    border = np.where(arr == 2)

    for line in range(len(border[0])):
        for j in range(border[1][line], len(arr[0])):
            arr[line - x_middle, j] = 2
    
    arr = arr.transpose()
    
    x2 = np.linspace(1, x_inner, x_inner)
    y2 = y_inner * gammainc(a_inner, x2 * 0.1)
    y2 = np.rint(y2)
    
    for n in range(0, x_inner):
        arr[int(y_outer - y2[n]), int(x2[n] + x_middle + x_inner - 1)] = 3
    
    arr = arr.transpose()

    border2 = np.where(arr == 3)

    for line in range(len(border2[0])):
        for j in range(border2[1][line], len(arr[0])):
                   arr[line - x_inner, j] = 3
    arr = arr.transpose()
    
    # beam-pipe area
    for i in range(24, 26):
        for j in range(30, 32):
            arr[i,j] = 0

    top = np.concatenate((arr, np.flip(arr,1)), axis = 1)
    result = np.concatenate((top, np.flip(top,0)), axis = 0)
    
    return result