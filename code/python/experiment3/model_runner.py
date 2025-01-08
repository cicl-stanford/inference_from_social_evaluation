import sys
sys.path.append('../analysis/')
import experiment_inference_analysis

import time
from datetime import datetime
import sys
import os
import numpy as np
import pandas as pd
import multiprocessing
from joblib import Parallel, delayed

models_blame = pd.read_csv('./intermediate_analyses/models_blame.csv')

if __name__ == "__main__":
	mixture_search = {'w': [.1, .5, .9], 'decision_beta': [.5, 9], 'rationality_beta': [.5, 9], 'k': [1]}
	start = time.time()
	poopy = Parallel(n_jobs=4)(delayed(models_inf(w, mixture_search, models_blame, ppt_df)) for w in mixture_search['w'])
	end = time.time(); print(end-start)