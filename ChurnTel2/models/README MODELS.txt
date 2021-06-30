classification_11_cols :
11 numerical cols, no data prep needed
Cols : 
['Conf Call', 'Messagerie Vocale', 'Points fidélité', 'SOS crédit',
       'Transfert Internet', 'Transfert Crédit', 'Service Roaming',
       'Connexion Internet', 'Orange Money', 'Mobicash Ooredoo', 'Mdinar']
code :
Pkl_Filename = "classification_11_cols.pkl"  

with open(Pkl_Filename, 'wb') as file:  
    pickle.dump(model, file)

xpred=np.array([5,7,6,5,5,5,1,9,6,6,7]) #example of input
model.predict(xpred.reshape(1,-1))
-------------------------------------------
recommender:
params (dataframe_of_scores,column) #column should be the same as in Cols
returns dict : top 5 (if available) ordered recommended services
code : 

#Loading the function
Pkl_Filename = "recommender.pkl"  
with open(Pkl_Filename, 'rb') as file:  
    recommender_fn = pickle.load(file)

#loading data
df=pd.read_excel('notes.xlsx')
d_rec=df.drop(columns=['client_id','Satisfait'])

#same columns as classification 11
print(list(recommender_fn(d_rec,'Messagerie Vocale').keys())) #gives u top 5 (if available) best options

for s in d_rec.columns:
    print(s,recommender_fn(d_rec,s)) # {service name : correlation with s}

-----------------------------------------------
classification_excel:
classification on all the excel file,

code : 

Pkl_Filename = "classification_excel.pkl"  
with open(Pkl_Filename, 'rb') as file:  
    RF = pickle.load(file)
Pkl_Filename = "ct.pkl"  
with open(Pkl_Filename, 'rb') as file:  
    ct = pickle.load(file)
Pkl_Filename = "scaler.pkl"  
with open(Pkl_Filename, 'rb') as file:  
    scaler = pickle.load(file)
Pkl_Filename = "imputer.pkl"  
with open(Pkl_Filename, 'rb') as file:  
    imputer = pickle.load(file)

#list of columns to keep
Pkl_Filename = "keep.pkl"  
with open(Pkl_Filename, 'rb') as file:  
    to_keep = pickle.load(file)

#Main split
df_init=pd.read_excel('data.xlsx') #ur file to predict
Y=df_init.loc[:200,'satisfied'] #i selected only 200 rows mel excel mte3na el original
X=df_init.loc[:200,to_keep]
X.drop(columns='Client_id',inplace=True)
X=np.array(ct.transform(X))
X=imputer.transform(X)
X[:,45:]=scaler.transform(X[:,45:])
ypred=RF.predict(X)
