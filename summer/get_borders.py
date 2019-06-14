import numpy as np
from scipy.special import gammainc

def get_borders(y_middle=10, x_middle=16, a_middle=0.01, y_inner=6, x_inner=8, a_inner=0.01):
    x = np.linspace(0, 5, 100)
    y = (y_middle - 1) * gammainc(a_middle, x)
    g = (y_inner - 1) * gammainc(a_inner, x)
    y = np.rint(y).astype(np.int8)
    g = np.rint(g).astype(np.int8)

    # ECAL outer borders
    y_outer = 26
    x_outer = 32
    s_outer = (y_outer, x_outer)
    
    arr = np.ones(s_outer, dtype = np.int8)

    for n in range(0, 100):
#         arr[(y_outer - 1) - y, (np.rint(x * ((x_middle - 1) / 5)) + x_outer - x_middle).astype(np.int8)] = 2
        x_current = (np.rint(x[n] * ((x_middle - 1) / 5)) + x_outer - x_middle).astype(np.int8)
        y_current = (y_outer - 1) - y[n]
        for m in range(y_current, y_outer):
            arr[m, x_current] = 2
   
    for n in range(0, 100):
        x_current = (np.rint(x[n] * ((x_inner - 1) / 5)) + x_outer - x_inner).astype(np.int8)
        y_current = (y_outer - 1) - g[n]
        for m in range(y_current, y_outer):
            arr[m, x_current] = 3
    
    # beam-pipe area
    arr[24:26, 30:32] = 0


    top = np.concatenate((arr, np.flip(arr,1)), axis = 1)
    result = np.concatenate((top, np.flip(top,0)), axis = 0)
    
    #np.set_printoptions(threshold=np.inf, linewidth=np.inf)  # turn off summarization, line-wrapping
    #with open("geometry_data.txt", 'w') as f:
    #    np.savetxt(f, result, fmt="%i", delimiter=' ', newline='\n', header='', footer='', comments='# ')
    
    #get_borders = print(arr)
    
    return result