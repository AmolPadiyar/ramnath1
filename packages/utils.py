import pandas as pd 
import numpy as np 
import pickle
import json

import warnings
warnings.filterwarnings("ignore")
import config


class MedicalInshorance():
    
    def __init__(self,age,sex,bmi,children,smoker,region):
        
    
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        # one hot Encoded
        self.region = 'region_'+ region
        
        
    def load_model(self):
        
        
        with open(config.json_file,'r') as f:
            self.JSON= json.load(f)
            
        #pickle
            
        with open(config.mode_file,'rb') as f:
            self.Decision_tr_model = pickle.load(f)
            
            
    def predict_output(self):
        self.load_model()
        
        #one hot encoded
        index_region = list(self.JSON['columns']).index(self.region)
        index_region
                
        array = np.zeros(len(self.JSON['columns']))
        
        array[0] = self.age
        array[1] = self.JSON['sex'][self.sex]
        array[2] = self.bmi
        array[3] = self.children
        array[4] = self.JSON['smoker'][self.smoker]
        array[index_region] = 1
                            
        print("show array****\n",array)
        
        prediction = round(self.Decision_tr_model.predict([array])[0],2)
        print("final output is -----",prediction)
        return prediction
        
        
        
age = 19.0
sex = 'male'
bmi = 27.9
children = 0.0
smoker = 'no'
# one hot Encoded

region = 'southwest' 
                
obj = MedicalInshorance(age,sex,bmi,children,smoker,region)

prediction = obj.predict_output()
# print('final output is :---',prediction)