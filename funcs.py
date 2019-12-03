import os
import sys
import json
import pickle
import pandas as pd
import numpy as np
import joblib
import random
from sklearn.linear_model import LogisticRegression

def make_prediction(res_dict):
    # import model
    clf = joblib.load('./clf.pkl')
    return clf
    # convert form into dataframe
    # clean form dataframe 
    # new_form_clnd = FUNC(new_form)
    # pred_class = clf.predict(new_form_clnd[0])
    # print('Predicted class:', pred_class)
    # if pred_class == 1:
    #     label_to_return = 'Russian Troll'
    # else:
    #     label_to_return = 'Not a Russian Troll'
    # return label_to_return                          