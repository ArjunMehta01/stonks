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
        self.r = Requests(code)
        self.name = self.r.getName()
        
        self.total_flairs = 0
    
    def findFlairs(self):
        for i in range(len(self.data)):
                if (self.name or self.code)in (self.data.loc[i,'Title'].upper()):
                    if self.data.loc[i,'Flair'] in self.flairs:
                        self.flairs[self.data.loc[i,'Flair']] += 1
                        self.total_flairs += 1
                    else:
                        self.flairs[self.data.loc[i,'Flair']] = 1
                        self.total_flairs += 1
    
    def return_prediction(self):
        voilitity = (self.flairs['Discussion'] + self.flairs['DD'] + self.flairs['YOLO'] + self.flairs['Options'] - self.flairs['Fundamentals']) / self.total_flairs
        try:
            score = (self.flairs['Gain'] - self.flairs['Loss'])*voilitity# 0 to 100
        except:
            score = 0

        t = self.r.getAnalysis()
        b = t['buy'] 
        s = t['sell']
        sb = t['strongBuy']
        ss = t['strongSell']
        finScore = (2*sb + b - s - 2*ss) /(b+s+sb+ss)

        return (finScore+score)/2














