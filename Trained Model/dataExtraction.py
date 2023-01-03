import pymongo
import numpy as np
import pandas as pd

client = pymongo.MongoClient("mongodb://embifiAdmin:embifi_1659709763@db.embifi.in:22058/embifi-native?authMechanism=DEFAULT&authSource=admin")
db = client['lms']
collection_schedules = db['collection_schedules']
collections = db['collections']

def extract(customer_id):
    
    req = collections.find({'application_id': customer_id})
    
    all_records = collection_schedules.find({'collection_id': customer_id})
    lst = list(all_records)
    df = pd.DataFrame(lst)
    
    X1= df['edi_amount'].sum()

    X12 = df['edi_amount'].loc[:29].sum()
    X13 = df['edi_amount'].loc[30:59].sum()
    X14 = df['edi_amount'].loc[60:89].sum()
    X15 = df['edi_amount'].loc[90:119].sum()
    X16 = df['edi_amount'].loc[120:149].sum()   
    X17 = df['edi_amount'].loc[150:179].sum()
    X18 = df['collected_amount'].loc[:29].sum()
    X19 = df['collected_amount'].loc[30:59].sum()
    X20 = df['collected_amount'].loc[60:89].sum()
    X21 = df['collected_amount'].loc[90:119].sum()
    X22 = df['collected_amount'].loc[120:149].sum()
    X23 = df['collected_amount'].loc[150:179].sum()
    a = (X12 - X18)
    b = (X13+X12)-(X18+X19)
    c = (X12+X13+X14)-(X18+X19+X20)
    d = (X12+X13+X14+X15)-(X18+X19+X20+X21)
    e = (X12+X13+X14+X15+X16)-(X18+X19+X20+X21+X22)
    f = (X12+X13+X14+X15+X16+X17)-(X18+X19+X20+X21+X22+X23)
    X6 = value_X6(a, X12)
    X7 = value_X7(b, X13)
    X8 = value_X8(c, X14)
    X9 = value_X9(d, X15)
    X10 = value_X10(e, X16)
    X11 = value_X11(f, X17)
    
    return np.array([X1, X6, X7, X8, X9, X10, X11, X12, X13, X14, X15, X16, X17, X18, X19, X20, X21, X22, X23])

    
    
def find_any(_id):
    cust_id = _id
    person = collection_schedules.find({'collection_id': cust_id},
                             {'_id': 0, 'edi_number':1, 'edi_amount':1, 'collected_amount':1,'os_principal':1})
    
    for x1 in person:
        print(x1)

     
def count_ppl(_id):
    cust_id = _id
    count= collection_schedules.count_documents(filter={'collection_id': cust_id})
    print(count)
    


def value_X6(a, X12):
    X6 = -1
    if a<=X12:
        X6 = X6
    elif a>= X12:
        X6 = (X6+2)  
    return X6
    
def value_X7(b, X13):
    X7 = -1
    if b<= X13:
        X7 = (X7)
    elif b>= X13:
        X7 = (X7+2)  
    elif b>=2*(X13):
        X7 = (X7+3)
    return X7
    
def value_X8(c, X14):
    X8 = -1
    if c<= X14:
        X8 = (X8)
    elif (X14<c<2*(X14)):
        X8 = (X8+2)  
    elif (2*(X14)<c<3*(X14)):
        X8 = (X8+3)
    elif (3*(X14)<c<4*(X14)):
        X8 = (X8+4)
    return X8


def value_X9(d, X15):
    X9 = -1
    if d<= X15:
        X9 = (X9)
    elif (X15<d<2*(X15)):
        X9 = (X9+2)  
    elif (2*(X15)<d<3*(X15)):
        X9 = (X9+3)
    elif (3*(X15)<d<4*(X15)):
        X9 = (X9+4)
    elif (4*(X15)<d<5*(X15)):
        X9 = (X9+5)
    elif (5*(X15)<d<6*(X15)):
        X9 = (X9+6)
    return X9
    
def value_X10(e, X16):
    X10 = -1
    if e<= X16:
        X10 = (X10)
    elif (X16<e<2*(X16)):
        X10 = (X10+2)  
    elif (2*(X16)<e<3*(X16)):
        X10 = (X10+3)
    elif (3*(X16)<e<4*(X16)):
        X10 = (X10+4)
    elif (4*(X16)<e<5*(X16)):
        X10 = (X10+5)
    elif (5*(X16)<e<6*(X16)):
        X10 = (X10+6)
    elif (6*(X16)<e<7*(X16)):
        X10 = (X10+7)
    return X10
        
def value_X11(f, X17):
    X11 = -1
    if f<= X17:
        X11 = (X11)
    elif (X17<f<2*(X17)):
        X11 = (X11+2)  
    elif (2*(X17)<f<3*(X17)):
        X11 = (X11+3)
    elif (3*(X17)<f<4*(X17)):
        X11 = (X11+4)
    elif (4*(X17)<f<5*(X17)):
        X11 = (X11+5)
    elif (5*(X17)<f<6*(X17)):
        X11 = (X11+6)
    elif (6*(X17)<f<7*(X17)):
        X11 = (X11+7)
    elif (7*(X17)<f<8*(X17)):
        X11 = (X11+8)
    
    return X11

    


