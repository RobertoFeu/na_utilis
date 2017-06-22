import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

wild_type = np.loadtxt('wt_lac.csv', skiprows=1, delimiter=',')
q18m=np.loadtxt('q18m_lac.csv', skiprows=1, delimiter=',')
q18a=np.loadtxt('q18a_lac.csv', skiprows=1, delimiter=',')
