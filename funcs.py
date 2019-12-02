import os
import sys
import json
import pickle

# combine seven issue predictors into dataframe 

# one hot encode predictors dataframe

def make_prediction(text=str):
    # import model
    clf = joblib.load('./filename.pkl')
    
    # convert form into dataframe
    new_form = pd.Dataframe({'content': [text],
                         'target': None,
                         'author': None,
                         'publish-date': None})

    # clean form dataframe 
    new_form_clnd = FUNC(new_form)


    pred_class = clf.predict(new_form_clnd[0]
    print('Predicted class:', pred_class)
    
    if pred_class == 1:
        label_to_return = 'Russian Troll'
    else:
        label_to_return = 'Not a Russian Troll'
    
    return label_to_return                          