import os
import sys
import json
import pickle
import pandas as pd
import numpy as np
import joblib
import random
from sklearn.linear_model import LogisticRegression

def make_prediction(res_size, res_racial, res_climate, res_budget, res_immigration, res_terrorism, res_gender):
    data = {'imiss_c_2016_1': res_immigration,
            'imiss_f_2016': res_terrorism,
            'imiss_l_2016': res_climate,
            'imiss_p_2016': res_budget,
            'imiss_u_2016': res_size,
            'imiss_x_2016': res_racial, 
            'imiss_y_2016': res_gender
            }
    df = pd.DataFrame(data, index=[0])
    print('dataframe created')
    print(df_clean)
    print(len(df_clean.columns))

    # clf = joblib.load('./clf.pkl')
    # pred = clf.predict(X)
    # print(pred)
    return 'res.html'