from flask import Flask
import pickle
import numpy as np


loaded_model = pickle.load(open("model","rb"))
app = Flask(__name__)

@app.route('/')
def load_model():
    return 'Example:/prediction/full_sq = 10.0/life_sq = 10.0/floor = 10.0'

@app.route('/prediction/full_sq = <float:full_sq>/life_sq = <float:life_sq>/floor = <float:floor>')
def show_result(full_sq,life_sq,floor):
    pred = loaded_model.predict(np.array([[full_sq,life_sq,floor]]))
    return 'The price is: {}'.format(pred[0])

import os

port = int(os.environ.get("PORT",5000))
app.run(host = '0.0.0.0', port=port)

