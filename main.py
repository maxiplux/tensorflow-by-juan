from pymongo import MongoClient
import numpy as np
import random
import json
from json import JSONEncoder

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
def solver(v,c):

    A = np.array(v)
    B = np.array(c)
    try:
        return np.linalg.inv(A).dot(B).tolist()
    except:
        print ("Error aqui, ")
        return  []


client = MongoClient("mongodb://root:example@localhost:27017")
db = client["matrix"]
matrix = db.matrix
for i in range(0,10*1000):
    key_random=random.randint(100,100*1000)
    v = [list(random.choices(range(15), k=3)), list(random.choices(range(15), k=3)), list(random.choices(range(15), k=3))]
    c= list(random.choices(range(15), k=3))
    solution=solver( v, c )
    #record={"v":v,"c":c,"solution":solution}
    record=json.dumps({"v":v,"c":c,"solution":solution})
    print ("este record es mio", record)
    if solution:
        x = matrix.insert_one({"v":v,"c":c,"solution":solution})
        #print (solution, record)
    if (i%100==0):
        print ("Vamos en I", i)
