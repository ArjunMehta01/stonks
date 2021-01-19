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


def count_one_two(file_name):
    """ Take in a file name and return counts of 1 and 2

    Args:
        file_name (string): a file name

    Returns:
        tuple: a tuple with the first position of count of two
                and the second position of count of one
    """ 
    count_two = 0
    count_one = 0
    with open(file_name, "r") as infile:
        while True:
            try:
                a_num_raw = infile.readline().strip()
                if a_num_raw != "":
                    a_num = int(a_num_raw)
                    if a_num == 2:
                        count_two += 1
                    elif a_num == 1:
                        count_one += 1
                elif a_num_raw == "":
                    break
            except EOFError:
                break
    
    return (count_two, count_one)

if __name__ == "__main__":
    a = get_dict("smallset.csv")
    print(a)
                

