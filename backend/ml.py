import torch
import torchtext
from torchtext.datasets import text_classification
import pandas

from Requests import Requests


class Analysis():
    def __init__(self, code):
        self.code = code
        self.data = pandas.read_csv('backend/posts.csv')
        self.flairs = {}
        total_flairs = 0

tester = Requests(code)
name = tester.getName()
t = tester.getAnalysis()
flairs = {}
total_flairs = 0

for i in range(len(data)):
        if (name or code)in (data.loc[i,'Title'].upper()):
            if data.loc[i,'Flair'] in flairs:
                flairs[data.loc[i,'Flair']] += 1
                total_flairs += 1
            else:
                flairs[data.loc[i,'Flair']] = 1
                total_flairs += 1


voilitity = (flairs['Discussion'] + flairs['DD'] + flairs['YOLO'] + flairs['Options'] - flairs['Fundamentals']) / total_flairs

try:
    score = flairs['Gain'] - flairs['Loss']# 0 to 100
except:
    score = 0


b = t['buy'] 
s = t['sell']
sb = t['strongBuy']
ss = t['strongSell']

finScore = (2*sb + b - s - 2*ss) 
print(finScore * voilitity)












