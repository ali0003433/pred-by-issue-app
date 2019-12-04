import os
import sys
import json
import pickle
import pandas as pd
import numpy as np
import joblib
import random
from sklearn.linear_model import LogisticRegression

def size_dummies(res_size):
    size1 = None
    size2 = None
    size3 = None
    size4 = None
    if res_size == '1':
        size1 = 1
        size2 = 0 
        size3 = 0
        size4 = 0
        return size1, size2, size3, size4
    elif res_size == '2':
        size1 = 0
        size2 = 1 
        size3 = 0
        size4 = 0
        return size1, size2, size3, size4
    elif res_size == '3': 
        size1 = 0
        size2 = 0 
        size3 = 1
        size4 = 0
        return size1, size2, size3, size4
    elif res_size == '4':
        size1 = 0
        size2 = 0 
        size3 = 0
        size4 = 1
        return size1, size2, size3, size4
    else: 
        return size1, size2, size3, size4
def racial_dummies(res_racial):
    racial1 = None
    racial2 = None
    racial3 = None
    racial4 = None
    if res_racial == '1':
        racial1 = 1
        racial2 = 0 
        racial3 = 0
        racial4 = 0
        return racial1, racial2, racial3, racial4
    elif res_racial == '2':
        racial1 = 0
        racial2 = 1 
        racial3 = 0
        racial4 = 0
        return racial1, racial2, racial3, racial4
    elif res_racial == '3': 
        racial1 = 0
        racial2 = 0 
        racial3 = 1
        racial4 = 0
        return racial1, racial2, racial3, racial4
    elif res_racial == '4':
        racial1 = 0
        racial2 = 0 
        racial3 = 0
        racial4 = 1 
        return racial1, racial2, racial3, racial4 
    else:
        return racial1, racial2, racial3, racial4 
def clm_dummies(res_climate): 
    clim1 = None
    clim2 = None
    clim3 = None
    clim4 = None 
    if res_climate == '1':
        clim1 = 1
        clim2 = 0 
        clim3 = 0
        clim4 = 0
        return clim1, clim2, clim3, clim4
    elif res_climate == '2':
        clim1 = 0
        clim2 = 1 
        clim3 = 0
        clim4 = 0
        return clim1, clim2, clim3, clim4
    elif res_climate == '3': 
        clim1 = 0
        clim2 = 0 
        clim3 = 1
        clim4 = 0
        return clim1, clim2, clim3, clim4
    elif res_climate == '4':
        clim1 = 0
        clim2 = 0 
        clim3 = 0
        clim4 = 1
        return clim1, clim2, clim3, clim4
    else:
        return clim1, clim2, clim3, clim4
def bgt_dummies(res_budget):
    bgt1 = None
    bgt2 = None
    bgt3 = None
    bgt4 = None
    if res_budget == '1':
        bgt1 = 1
        bgt2 = 0 
        bgt3 = 0
        bgt4 = 0
        return bgt1, bgt2, bgt3, bgt4
    elif res_budget == '2':
        bgt1 = 0
        bgt2 = 1 
        bgt3 = 0
        bgt4 = 0
        return bgt1, bgt2, bgt3, bgt4
    elif res_budget == '3': 
        bgt1 = 0
        bgt2 = 0 
        bgt3 = 1
        bgt4 = 0
        return bgt1, bgt2, bgt3, bgt4
    elif res_budget == '4':
        bgt1 = 0
        bgt2 = 0 
        bgt3 = 0
        bgt4 = 1 
        return bgt1, bgt2, bgt3, bgt4
    else: 
        return bgt1, bgt2, bgt3, bgt4
def imm_dummies(res_immigration):
    imm1 = None
    imm2 = None
    imm3 = None
    imm4 = None
    if res_immigration == '1':
        imm1 = 1
        imm2 = 0 
        imm3 = 0
        imm4 = 0
        return imm1, imm2, imm3, imm4
    if res_immigration == '2':
        imm1 = 0
        imm2 = 1 
        imm3 = 0
        imm4 = 0
        return imm1, imm2, imm3, imm4
    if res_immigration == '3': 
        imm1 = 0
        imm2 = 0 
        imm3 = 1
        imm4 = 0
        return imm1, imm2, imm3, imm4
    if res_immigration == '4':
        imm1 = 0
        imm2 = 0 
        imm3 = 0
        imm4 = 1
        return imm1, imm2, imm3, imm4
    else: 
        return imm1, imm2, imm3, imm4
def trr_dummies(res_terrorism):
    trr1 = None
    trr2 = None
    trr3 = None
    trr4 = None
    if res_terrorism == '1':
        trr1 = 1
        trr2 = 0 
        trr3 = 0
        trr4 = 0
        return trr1, trr2, trr3, trr4
    elif res_terrorism == '2':
        trr1 = 0
        trr2 = 1 
        trr3 = 0
        trr4 = 0
        return trr1, trr2, trr3, trr4
    elif res_terrorism == '3': 
        trr1 = 0
        trr2 = 0 
        trr3 = 1
        trr4 = 0
        return trr1, trr2, trr3, trr4
    elif res_terrorism == '4':
        trr1 = 0
        trr2 = 0 
        trr3 = 0
        trr4 = 1  
        return trr1, trr2, trr3, trr4
    else: 
        return trr1, trr2, trr3, trr4
def gdr_dummies(res_gender):
    gdr1 = None
    gdr2 = None
    gdr3 = None
    gdr4 = None
    if res_gender == '1':
        gdr1 = 1
        gdr2 = 0 
        gdr3 = 0
        gdr4 = 0
        return gdr1, gdr2, gdr3, gdr4
    elif res_gender == '2':
        gdr1 = 0
        gdr2 = 1 
        gdr3 = 0
        gdr4 = 0
        return gdr1, gdr2, gdr3, gdr4
    elif res_gender == '3': 
        gdr1 = 0
        gdr2 = 0 
        gdr3 = 1
        gdr4 = 0
        return gdr1, gdr2, gdr3, gdr4
    elif res_gender == '4':
        gdr1 = 0
        gdr2 = 0 
        gdr3 = 0
        gdr4 = 1 
        return gdr1, gdr2, gdr3, gdr4
    else:
        return gdr1, gdr2, gdr3, gdr4

def make_prediction(res_size, res_racial, res_climate, res_budget, res_immigration, res_terrorism, res_gender):
    size1, size2, size3, size4 =  size_dummies(res_size)
    racial1, racial2, racial3, racial4 = racial_dummies(res_racial)
    clim1, clim2, clim3, clim4 = clm_dummies(res_climate)
    bgt1, bgt2, bgt3, bgt4 = bgt_dummies(res_budget)
    imm1, imm2, imm3, imm4 = imm_dummies(res_immigration)
    trr1, trr2, trr3, trr4 = trr_dummies(res_terrorism)
    gdr1, gdr2, gdr3, gdr4 = gdr_dummies(res_gender)

    data = {'imiss_c_2016_1.0': imm1,
            'imiss_c_2016_2.0': imm2,
            'imiss_c_2016_3.0': imm3, 
            'imiss_c_2016_4.0': imm4, 
            'imiss_f_2016_1.0': trr1,
            'imiss_f_2016_2.0': trr2,
            'imiss_f_2016_3.0': trr3, 
            'imiss_f_2016_4.0': trr4,
            'imiss_l_2016_1.0': clim1,
            'imiss_l_2016_2.0': clim2,
            'imiss_l_2016_3.0': clim3, 
            'imiss_l_2016_4.0': clim4,
            'imiss_p_2016_1.0': bgt1,
            'imiss_p_2016_2.0': bgt2,
            'imiss_p_2016_3.0': bgt3, 
            'imiss_p_2016_4.0': bgt4,
            'imiss_u_2016_1.0': size1,
            'imiss_u_2016_2.0': size2,
            'imiss_u_2016_3.0': size3, 
            'imiss_u_2016_4.0': size4,
            'imiss_x_2016_1.0': racial1,
            'imiss_x_2016_2.0': racial2,
            'imiss_x_2016_3.0': racial3, 
            'imiss_x_2016_4.0': racial4,
            'imiss_y_2016_1.0': gdr1,
            'imiss_y_2016_2.0': gdr2,
            'imiss_y_2016_3.0': gdr3, 
            'imiss_y_2016_4.0': gdr4,
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
        prediction = 'Trump'
        return prediction
    elif prediction == 3.0:
        print('Other behavior')
        prediction = 'A third party'
        return prediction
    else:
        return prediction