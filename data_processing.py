"""
Author: Albert Dinh

Source Visited: 
    The following link has information about how to read line by line from a csv file:
        https://www.geeksforgeeks.org/load-csv-data-into-list-and-dictionary-using-python/
"""
import csv

def get_dict(csv_in):
    with open(csv_in, 'r') as info: 
        count = 0   
        data_dict = dict()
        for line in csv.reader(info):
            if count == 0:
                for attribute in line:
                    data_dict[attribute] = []
            else:
                list_key = list(data_dict.keys())
                for i in range(len(list_key)):
                    data_dict[list_key[i]].append(line[i])
            count += 1
    
    return data_dict


def sort_by_date():
    pass

if __name__ == "__main__":
    a = get_dict("smallset.csv")
    print(a)
                

