from django.shortcuts import render
from django.http import JsonResponse
from .models import PredResults
import pandas as pd
import numpy as np
import dill as pk
import pickle
from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from django.views.decorators.csrf import csrf_exempt

def predict(request):
    return render(request, 'predict.html')

@csrf_exempt
def predict_excel(request):

     
    Pkl_Filename = r"C:\Users\Bolbol\Desktop\ChrunTel2\models\classification_excel.pkl"
    with open(Pkl_Filename, 'rb') as file:
        RF = pickle.load(file)
    Pkl_Filename = r"C:\Users\Bolbol\Desktop\ChrunTel2\models\ct.pkl"
    with open(Pkl_Filename, 'rb') as file:
        ct = pickle.load(file)
    Pkl_Filename = r"C:\Users\Bolbol\Desktop\ChrunTel2\models\scaler.pkl"
    with open(Pkl_Filename, 'rb') as file:
        scaler = pickle.load(file)
    Pkl_Filename = r"C:\Users\Bolbol\Desktop\ChrunTel2\models\imputer.pkl"
    with open(Pkl_Filename, 'rb') as file:
        imputer = pickle.load(file)

    # list of columns to keep
    Pkl_Filename = r"C:\Users\Bolbol\Desktop\ChrunTel2\models\keep.pkl"
    with open(Pkl_Filename, 'rb') as file:
        to_keep = pickle.load(file)

    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    # Main split
    df_init = pd.read_excel(filename)  # ur file to predict
    Names=list(df_init.loc[:10,'Name'])



    X = df_init.loc[:10, to_keep]

    X.drop(columns='Client_id', inplace=True)
    X = np.array(ct.transform(X))
    X = imputer.transform(X)
    X[:, 45:] = scaler.transform(X[:, 45:])
    ypred = RF.predict(X)

    SatisfactionList = []
    for i in ypred:
        if (i == 0):
            SatisfactionList.append("Satisfied")
        else:
            SatisfactionList.append("Unsatisfied")

    return JsonResponse({'Names': Names,'SatisfactionList':SatisfactionList})


def predict_chances(request):

    if request.POST.get('action') == 'post':
        # Receive data from client

        Conference_call = int(request.POST.get('Conference_call'))
        Messagerie_Vocale = int(request.POST.get('Messagerie_Vocale'))
        Points_fidelite = int(request.POST.get('Points_fidelite'))
        SOS_Credit = int(request.POST.get('SOS_Credit'))
        Transfert_Internet = int(request.POST.get('Transfert_Internet'))
        Transfert_Credit = int(request.POST.get('Transfert_Credit'))
        Service_Roaming = int(request.POST.get('Service_Roaming'))
        Connexion_Internet = int(request.POST.get('Connexion_Internet'))
        Orange_Money = int(request.POST.get('Orange_Money'))
        Mobicash_Ooredoo = int(request.POST.get('Mobicash_Ooredoo'))
        Mdinar = int(request.POST.get('Mdinar'))

        dict = {Conference_call: "Conf Call", Messagerie_Vocale: "Messagerie Vocale",
                Points_fidelite: "Points fidélité", SOS_Credit: "SOS crédit", Transfert_Internet: "Transfert Internet",
                Transfert_Credit: "Transfert Crédit", Service_Roaming: "Service Roaming",
                Connexion_Internet: "Connexion Internet", Orange_Money: "Orange Money",
                Mobicash_Ooredoo: "Mobicash Ooredoo",
                Mdinar: "Mdinar"}

        # Unpickle model



        modelClassif = pd.read_pickle(
            r"C:\Users\Bolbol\Desktop\ChrunTel2\models\classification_11_cols.pkl")

        # Unpack Recommend
        Pkl_Filename =r"C:\Users\Bolbol\Desktop\ChrunTel2\models\recommend_dill.pkl"
        with open(Pkl_Filename, 'rb') as file:
            recommender_fn = pk.load(file)
        df = pd.read_excel(r'C:\Users\Bolbol\Desktop\ChrunTel2\models\notes.xlsx')
        d_rec = df.drop(columns=['client_id', 'Satisfait'])

        XPredClass = np.array(
            [Conference_call, Messagerie_Vocale, Points_fidelite, SOS_Credit, Transfert_Internet, Transfert_Credit,
             Service_Roaming, Connexion_Internet, Orange_Money, Mobicash_Ooredoo,
             Mdinar])

        rec=list(recommender_fn(d_rec, dict[np.max(XPredClass)]).keys())
        Classification = modelClassif.predict(XPredClass.reshape(1, -1))[0]


        if Classification == 1:
            R = "Satisfied"

        else:
            R = "Unsatisfied"


        return JsonResponse({'result': R,'recommended':rec})



def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)


def classifIntern(request):
    return render(request, 'classifIntern.html')

def index(request):
    return render(request,"chatroom.html")



def External(request):
    return render(request, 'External.html')