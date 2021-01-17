import torch
import torchtext
from torchtext.datasets import text_classification
import pandas



# tokenize = lambda x: x.split()


# quote = torchtext.data.Field(sequential=True, use_vocab=True, tokenize=tokenize, lower=True)
# score = torchtext.data.Field(sequential=True, use_vocab=True)


# fields = {'quote': ('q', quote), 'score': ('s', score)}

# train_data, test_data = torchtext.data.TabularDataset.splits(path='mydata', train ='train.csv', test='test.csv', format='csv', fields=fields)


data = pandas.read_csv('posts.csv')

for row in data df.iterrows():
    print(row)

data['Sentiment'] = sentiment


