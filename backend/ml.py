import torch
import torchtext
from torchtext.datasets import text_classification
import pandas

from Requests import Requests



# tokenize = lambda x: x.split()


# quote = torchtext.data.Field(sequential=True, use_vocab=True, tokenize=tokenize, lower=True)
# score = torchtext.data.Field(sequential=True, use_vocab=True)


# fields = {'quote': ('q', quote), 'score': ('s', score)}

# train_data, test_data = torchtext.data.TabularDataset.splits(path='mydata', train ='train.csv', test='test.csv', format='csv', fields=fields)


data = pandas.read_csv('backend/posts.csv') # assume 
code = 'TSLA'

tester = Requests(code)
name = tester.getName()
flairs = {}
#lookup stonk name

for i in range(len(data)):
        if (name or code)in (data.loc[i,'Title'].upper()):
            print(i)
            if data.loc[i,'Flair'] in flairs:
                flairs[data.loc[i,'Flair']] += 1
            else:
                flairs[data.loc[i,'Flair']] = 1

print(flairs)
                






