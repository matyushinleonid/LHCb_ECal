import numpy as np
from objective import black_box
from skopt import gp_minimize
from skopt.learning import GaussianProcessRegressor
from skopt.learning.gaussian_process.kernels import RBF, WhiteKernel
import json

with open('params.txt') as q:
        params = json.load(q)
        globals().update(params)
        
def optimize(x0, y0, n_calls):

    estimator = GaussianProcessRegressor(alpha=1e-4, normalize_y=True, noise='gaussian', n_restarts_optimizer=10, kernel=RBF())

    w = gp_minimize(black_box,
                [(low, high)] * dim,
                base_estimator=estimator,
                acq_func="EI", 
                n_calls=n_calls, 
                verbose=False,
                x0=x0,
                y0=y0,
                n_random_starts=1, 
                n_jobs=-1)
    return w.x_iters, w.func_vals.tolist()
