# ! pip install uproot --user

import uproot as uproot
import numpy as np
import pandas as pd
import os
from pathlib import Path

logs_path = Path(os.environ['LOGS_DIR'])
output_file = logs_path / "output.txt"

data_pGUN = uproot.open('GaussTuple_30000000.root')['DelphesTuple']['Res'].pandas.df()

def get_section(data, section, border_modules=0):
    border_x = [323.2, 969.6, 1939.2, 3878.4]
    border_y = [323.2, 727.2, 1212.0, 3151.2]

    if section == 'inner':
        i=0
    elif section == 'middle':
        i=1
    elif section == 'outer':
        i=2
    else:
        print('section must be inner, middle or outer')
        return None
    
    return data[(np.abs(data.xRec) < border_x[i+1] - 121.2*border_modules) & \
                   (np.abs(data.yRec) < border_y[i+1] - 121.2*border_modules) & \
                  ((np.abs(data.xRec) > border_x[i] + 121.2*border_modules) | \
                    (np.abs(data.yRec) > border_y[i] + 121.2*border_modules))]

def get_std(data, border_modules=1):
    i, sec_name = 0, 'inner'
    df = get_section(data, sec_name, border_modules=border_modules)

    arr = df.xRec - df.xGen - df.thetaXGen * (df.zRec - df.zGen)
    res = arr.std()
    with open(output_file, "w+") as f:
        f.write(str(res))
    return res
        
print(get_std(data_pGUN, border_modules=1))
