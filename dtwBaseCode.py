#This is a placeholder
import os
import numpy as np
from dtaidistance import dtw
import sys

###First step is to read in the file :

def extract_data(filename):
    #data =  []
    with open(filename) as f:
        file_data = f.read() #read the whole file and save to variable data
        data = (file_data.split('-------------------------------------------------'))
        #print("xxxxxxxxxxxxxxx")
    del data[0]
    #data has all the values seperated
    ##Next we need to split the data to find new stuff.
    class_label = []
    object_id = []
    sign = []
    X_train = []

    for example in data:
        lines = example.split("\n",6)
        object_id.append(lines[1].replace('object ID: ',''))
        class_label.append(lines[2].replace('class label: ',''))
        sign.append(lines[3].replace('sign meaning: ',''))
        temp = lines[-1].replace('\t','').replace('\n','').replace(' ',' ')

        temp2 = temp.split('   ')
        temp2 = temp2[1:]

        temp4 = [float(i) for i in temp2]
        temp4 = np.array(temp4)

        X_train.append(temp4.reshape(int(len(temp4)/2),2))

    X_train = np.array(X_train,dtype=object)

    print(X_train[0])






if __name__ == '__main__':
    extract_data(sys.argv[1])
