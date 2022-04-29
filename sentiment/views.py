from ctypes import util
from difflib import context_diff
from email import utils
from multiprocessing import context
from pprint import PrettyPrinter
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .models import Editors
from scipy import stats
from collections import OrderedDict
from collections import Counter
from . import utils
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

import csv
import pandas as pd
# Creating views

g_posi_cc = 0
g_negi_cc = 0
g_neut_cc = 0

r_posi_cc = 0
r_negi_cc = 0
r_neut_cc = 0

k_posi_cc = 0
k_negi_cc = 0
k_neut_cc = 0

s_posi_cc = 0
s_negi_cc = 0
s_neut_cc = 0
ii = 0
def home(request):
    return render(request, "sentiment/home.html")

def index(request):
    
    if request.method == "POST":
        # op=grid(request)

        myfile = request.FILES['myfile']
    
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        data = pd.read_csv(fs.open(filename)) 
        sortedData = data.sort_values(["Reviewed Year"])
        Sorteddates = {}
        ratingCountMonth = {}

        for idx in sortedData.index:
            month_year = [data["Reviewed Year"][idx], data["Reviewed Month"][idx]]
            date = tuple(month_year)
            rating_int = int(data["Rating"][idx])
            
            if date in Sorteddates:
                Sorteddates[date] +=1
            else:
                Sorteddates[date] = 1

            if date in ratingCountMonth:
                ratingCountMonth[date][rating_int-1] +=1
            else:
                ratingDict = [0,0,0,0,0]
                ratingCountMonth[date] = ratingDict

        reviewCount = {}
        reviewCount = OrderedDict(sorted(ratingCountMonth.items()))

        finalDict = {}
        finalDict = OrderedDict(sorted(Sorteddates.items()))

        dd = {}
        finalReviewCount = {}

        for key, value in reviewCount.items():
            month = utils.months_maping(key[1])
            finalReviewCount[ month + "-" + str(key[0]) ] = value

        for key, value in finalDict.items():
            month = utils.months_maping(key[1])
            dd[ month + "-" + str(key[0]) ] = value

        # rating graph
        rating = data['Rating'].tolist()
        ratingCount = Counter(rating)
        ordRatingCount = OrderedDict(sorted(ratingCount.items()))
        final_rating_count = dict(ordRatingCount)
        global g_posi_cc
        global g_negi_cc 
        global g_neut_cc
        
        global r_posi_cc
        global r_negi_cc 
        global r_neut_cc
        
        global k_posi_cc
        global k_negi_cc 
        global k_neut_cc
        
        global s_posi_cc
        global s_negi_cc 
        global s_neut_cc
        global ii
        for i in data["Review"][:5]:
            # for j in range(10):
            ii += 1
            print(ii)
            if grid(request, i) == "Positive":
                g_posi_cc += 1
            if grid(request, i) == "Neutral":
                g_neut_cc  += 1
            if grid(request, i) == "Negative":
                g_negi_cc += 1

            if ridge(request, i) == "Positive":
                r_posi_cc += 1
            if ridge(request, i) == "Neutral":
                r_neut_cc  += 1
            if ridge(request, i) == "Negative":
                r_negi_cc += 1
            
            if kneighbor(request, i) == "Positive":
                k_posi_cc += 1
            if kneighbor(request, i) == "Neutral":
                k_neut_cc  += 1
            if kneighbor(request, i) == "Negative":
                k_negi_cc += 1

            if svc(request, i) == "Positive":
                s_posi_cc += 1
            if svc(request, i) == "Neutral":
                s_neut_cc  += 1
            if svc(request, i) == "Negative":
                s_negi_cc += 1
        # print("grid")     
        # print("positive",g_posi_cc)
        # print("negative",g_negi_cc)
        # print("neutral",g_neut_cc)
        # print("ridge")
        # print("positive",r_posi_cc)
        # print("negative",r_negi_cc)
        # print("neutral",r_neut_cc)
        # print("kneighbor")
        # print("positive",k_posi_cc)
        # print("negative",k_negi_cc)
        # print("neutral",k_neut_cc)
        # print("svm")
        # print("positive",s_posi_cc)
        # print("negative",s_negi_cc)
        # print("neutral",s_neut_cc)
        g_data=[]
        g_data.append(g_negi_cc)
        g_data.append(g_neut_cc)
        g_data.append(g_posi_cc)
        
        r_data=[]
        r_data.append(r_negi_cc)
        r_data.append(r_neut_cc)
        r_data.append(r_posi_cc)
        
        k_data=[]
        k_data.append(k_negi_cc)
        k_data.append(k_neut_cc)
        k_data.append(k_posi_cc)
        
        s_data=[]
        s_data.append(s_negi_cc)
        s_data.append(s_neut_cc)
        s_data.append(s_posi_cc)
        
        context = {
            'data' : dd,
            'final_rating_count' : final_rating_count,
            'reviewCount' : finalReviewCount,
            # 'ans':op,
            'g_data':g_data,
            'r_data':r_data,
            'k_data':k_data,
            's_data':s_data,
                       
        }

        return render(request, "sentiment/index.html",context)

    return render(request, "sentiment/home.html")


# Test input 
def testInput(request):
    print("in test inp")
    if request.method == 'POST' : 

        modelName = request.POST.get('modelName')
        inputText = request.POST.get('inputText')

        data = {
            'input' : inputText,
        }

        if modelName == "ridgeClass":
            op = ridge(request,inputText)
            data.update({'name':'Ridge Classifier'})
            data.update({'sentiment':op})

        elif modelName == "randomForest":
            op = grid(request,inputText)
            data.update({'name':'Random Forest'})
            data.update({'sentiment':op})

        elif modelName == "kNeighbors":
            op = kneighbor(request,inputText)
            data.update({'name':'K-Neighbors'})
            data.update({'sentiment':op})

        else:
            op = svc(request,inputText)
            data.update({'name':'SVC'})
            data.update({'sentiment':op})
                
        return JsonResponse(data, safe=False)

    return render(request, "sentiment/inputtest.html")



def grid(request,inp):
    modell=pickle.load(open("grid_model_with_2_hp_22_v2.sav", "rb"))
    # inps=[]
    # inps.append(request.GET["User_input"])
    inps=inp
    # print(inps)
    # for i in inps:
    vector=pickle.load(open('vector.sav', 'rb'))
    ans=processs(vector,modell,inps)
    return ans
    # return render(request,'sentiment/result.html',{'ans':ans})

def ridge(request,inp):
    print(".......,.,.,.,.,as,.sd,.sd,.sd,.sd,.sd.,sd.,sd,.sd,.sd,.")
    modell=pickle.load(open("ridge_classifier.sav", "rb"))
    # inps=[]
    # inps.append(request.GET["User_input"])
    inps=inp
    # print(inps)
    # for i in inps:
    vector=pickle.load(open('vector.sav', 'rb'))
    ans=processs(vector,modell,inps)
    return ans
    # return render(request,'result1.html',{'ans':ans})

def kneighbor(request,inp):
    print(".......,.,.,.,.,as,.sd,.sd,.sd,.sd,.sd.,sd.,sd,.sd,.sd,.")
    modell=pickle.load(open("kneighbor.sav", "rb"))
    # inps=[]
    # inps.append(request.GET["User_input"])
    inps=inp
    # print(inps)
    # for i in inps:
    vector=pickle.load(open('vector.sav', 'rb'))
    ans=processs(vector,modell,inps)
    return ans
    # return render(request,'result1.html',{'ans':ans})

def svc(request,inp):
    print(".......,.,.,.,.,as,.sd,.sd,.sd,.sd,.sd.,sd.,sd,.sd,.sd,.")
    modell=pickle.load(open("svc_classifier.sav", "rb"))
    # inps=[]
    # inps.append(request.GET["User_input"])
    inps=inp
    # print(inps)
    # for i in inps:
    vector=pickle.load(open('vector.sav', 'rb'))
    ans=processs(vector,modell,inps)
    # return render(request,'result1.html',{'ans':ans})
    return ans

def processs(vector,model,inputt):
# def customm(inputt):
    # vector=CountVectorizer()
#     inp=input("Enter a Sentence: ")
    # print(inputt," :: ")
    train_fina=[]
    lm = WordNetLemmatizer()
    stopword=set(stopwords.words("english"))
    wor=re.sub("[^A-Za-z]",' ',str(inputt))
    wor=wor.lower()    
    wor=wor.split()
    wor = [lm.lemmatize(word) for word in wor if word not in set(stopwords.words('english'))]
    tex=[]
    for ijx in wor:
        if ijx not in stopword:
            tex.append(lm.lemmatize(ijx))
    train_fina.append(" ".join(tex))
    op=''
    test=vector.transform(train_fina)
    predic=model.predict(test)
    # print(predic)
    if(predic[0] == 2):
        op="Positive"
        # print("Positive")
    if(predic[0] == 1):
        op="Neutral"
        # print("Neutral")
    if(predic[0] == 3): 
        op="Negative"
        # print("Negative")
    return op
