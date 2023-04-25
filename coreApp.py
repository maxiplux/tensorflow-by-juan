from pymongo import MongoClient

import numpy as np
import tensorflow as tf
import plotly.graph_objects as go
import random
import json
from json import JSONEncoder

print ("Start")
client = MongoClient("mongodb://root:example@localhost:27017")
db = client["matrix"]
matrix = db.matrix

print (db.matrix.bios.find().limit( 5 ))
print("End")
