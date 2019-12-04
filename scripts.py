import os
import sys
import json
import pickle
import pandas as pd
import numpy as np
import joblib
import random
from sklearn.linear_model import LogisticRegression

def dummies(res):
    result = [0,0,0,0]
    if int(res) > 1:
        result[int(res)-2] = 1
    return result

def make_prediction(res_size, res_racial, res_climate, res_budget, res_immigration, res_terrorism, res_gender):
    size1, size2, size3, size4 =  dummies(res_size)
    racial1, racial2, racial3, racial4 = dummies(res_racial)
    clim1, clim2, clim3, clim4 = dummies(res_climate)
    bgt1, bgt2, bgt3, bgt4 = dummies(res_budget)
    imm1, imm2, imm3, imm4 = dummies(res_immigration)
    trr1, trr2, trr3, trr4 = dummies(res_terrorism)
    gdr1, gdr2, gdr3, gdr4 = dummies(res_gender)
    data = {'imiss_c_2016_2.0': imm1,
            'imiss_c_2016_3.0': imm2,
            'imiss_c_2016_4.0': imm3, 
            'imiss_c_2016_8.0': imm4, 
            'imiss_f_2016_2.0': trr1,
            'imiss_f_2016_3.0': trr2,
            'imiss_f_2016_4.0': trr3, 
            'imiss_f_2016_8.0': trr4,
            'imiss_l_2016_2.0': clim1,
            'imiss_l_2016_3.0': clim2,
            'imiss_l_2016_4.0': clim3, 
            'imiss_l_2016_8.0': clim4,
            'imiss_p_2016_2.0': bgt1,
            'imiss_p_2016_3.0': bgt2,
            'imiss_p_2016_4.0': bgt3, 
            'imiss_p_2016_8.0': bgt4,
            'imiss_u_2016_2.0': size1,
            'imiss_u_2016_3.0': size2,
            'imiss_u_2016_4.0': size3, 
            'imiss_u_2016_8.0': size4,
            'imiss_x_2016_2.0': racial1,
            'imiss_x_2016_3.0': racial2,
            'imiss_x_2016_4.0': racial3, 
            'imiss_x_2016_8.0': racial4,
            'imiss_y_2016_2.0': gdr1,
            'imiss_y_2016_3.0': gdr2,
            'imiss_y_2016_4.0': gdr3, 
            'imiss_y_2016_8.0': gdr4,
            }
    df = pd.DataFrame(data, index=[0])
    print('dataframe created')
    print(df)
    print('df length:', len(df.columns))
    clf = joblib.load('./clf_2.pkl')
    prediction = clf.predict(df)
    print(prediction)
    if prediction == 1.0:
        print('Clinton')
        prediction = 'Hillary Clinton'
        return prediction
    elif prediction == 2.0:
        print('Donald J. Trump')
        prediction = 'Donald J. Trump'
        return prediction
    elif prediction == 3.0:
        print('Other behavior')
        prediction = 'A third party'
        return prediction
    else:
        return prediction