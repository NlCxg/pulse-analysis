import numpy as np
import os
from scipy.io import loadmat
from scipy import stats
path_health = './health/'
path_dm = './hyper/'

mat_hea = [os.path.join(path_health, f) for f in os.listdir(path_health) if f.endswith('.mat')]
mat_dm = [os.path.join(path_dm, f) for f in os.listdir(path_dm) if f.endswith('.mat')]

data_hea = np.array([]).reshape(0, 9)
for temp_hea in mat_hea:
    data_tempt = loadmat(temp_hea)
    data_tempt = data_tempt['tempff']
    data_hea = np.vstack((data_hea, data_tempt))

data_dm = np.array([]).reshape(0, 9)
for temp_dm_t in mat_dm:
    temp_dm_t = loadmat(temp_dm_t)
    temp_dm_t = temp_dm_t['tempff']
    data_dm = np.vstack((data_dm, temp_dm_t))

results = []
for kk in range(6):  #range(data_dm.shape[1]):
    value_hea = data_hea[:, kk]
    value_die = data_dm[:, kk]
    t_stat, p_value = stats.ttest_ind(value_hea, value_die)
    results.append(p_value)
    alpha = 0.05
    if p_value < alpha:
        print("抑郁存在显著差异（拒绝零假设）")
    else:
        print(f"{kk} + {p_value}")

print(results)