import pandas as pd
from predict import predict


data = pandas.read_csv('working/week.csv')
dictionary = {}

for i in range(len(self.data)):
    predict(data.loc[i,'title'], 'model.py', dictionary, ngrams=2)
    predict(data.loc[i,'body'], 'model.py', dictionary, ngrams=2)