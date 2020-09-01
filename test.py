import numpy as np
import pandas as pd

data = pd.DataFrame([])
print(np.arange(0, 4))
for i in np.arange(0, 4):
    if i + 1 != 0:
        data = data.append(pd.DataFrame({'A': i, 'B': i + 1}, index=[0]), ignore_index=True)
    else:
        data = data.append(pd.DataFrame({'A': i}, index=[0]), ignore_index=True)

print(data.head())