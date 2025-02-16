
import pandas as pd
import numpy as np
import sklearn
from sklearn import *
import os,glob
def createModel(path):
    data=pd.read_csv(path)
    data=data.fillna("")
    data=data.to_numpy()
    trainData=[]
    trainData2=[]
    for i in range(len(data)):
        if data[i][1]!='':
            trainData2.append(i+1)
    for d in data:
        if d[1]!='':
            temp=[]
            temp.append(d[5])
            temp.append(d[6])
            temp.append(d[8])
            temp.append(d[9])
            trainData.append(temp)
        
        else:
            pass
        
        
        
    
    model=svm.SVC()
    model.fit(trainData,trainData2)
    
    return model
path = r"C:\Users\xuzih\OneDrive\桌面\stan's project\Data\*.csv"
modelNames=[]
modelPaths=[]
models=[]
for fname in glob.glob(path):
    modelPaths.append(fname)
    name=str(fname)
    name=name.replace(r"C:\Users\xuzih\OneDrive\桌面\stan's project\Data","")
    name=name.replace('.csv',"")
    name=name[1:len(name)]
    modelNames.append(name)
    models.append(createModel(fname))
#creates linear regression for a category
def test(index,data):
    trainData=[]
    
    for d in data:
         if d[1]!='':
            temp=[]
            temp.append(d[index])
            trainData.append(temp)
    
    trainData2=[]
    for i in range(len(data)):
         if data[i][1]!='':
            trainData2.append(i+1)
    model=svm.SVC()
    model.fit(trainData,trainData2)
    return model
#returns array full of linear regression model of every category
def findChange(path):
    data=pd.read_csv(path)
    data=data.fillna("")
    data=data.to_numpy()
    Models=[]
    Models.append(test(5,data))
    Models.append(test(6,data))
    Models.append(test(8,data))
    Models.append(test(9,data))
    return Models
def useModel(index,arr2d):
    suggestion=''
    prediction=models[index].predict(arr2d)
    prediction=prediction[0]
    data=pd.read_csv(modelPaths[index])
    data=data.fillna("")
    data=data.to_numpy()
    percentage=prediction/float(len(data))*100
    percentage=round(percentage,2)
    testModels=findChange(modelPaths[index])
    cats=['pictures','videos','# ofwords in description','keywords in description']
    indexofSuggestion=0
    p=0
    for i in range(len(testModels)):
        temp=[]
        temp.append(arr2d[0][i])
        prediction=testModels[i].predict([temp]) 
        if(prediction>p):
            indexofSuggestion=i
            p=prediction

    if(percentage<=10):
        suggestion='Your item should do very good, it aligns with the top 10 percent of items in its category'+"\nyou might want to change "+cats[indexofSuggestion]
    elif(percentage<=50):
        suggestion='Your item should ok, it aligns with the better half of these items in its categories'+"\nyou might want to change "+cats[indexofSuggestion]
    else:
        suggestion='Your item might not fare to well against its competition'+"\nyou might want to change "+cats[indexofSuggestion]
    return [suggestion,str(percentage)+'%']
