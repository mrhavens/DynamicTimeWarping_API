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
    coordiante_points = []

    for example in data:
        lines = example.split("\n",6)
        object_id.append(lines[1].replace('object ID: ',''))
        class_label.append(lines[2].replace('class label: ',''))
        sign.append(lines[3].replace('sign meaning: ',''))
        temp = lines[-1].replace('\t','').replace('\n','').replace(' ',' ')

        temp2 = temp.split('   ')
        temp2 = temp2[1:]
        temp2 = [i.replace(' ','') for i in temp2]
        temp3 = [float(i) for i in temp2 if i]
        #temp4 = [float(i) for i in temp3]
        temp4 = np.array(temp3)

        coordiante_points.append(temp4.reshape(int(len(temp4)/2),2))

    coordiante_points = np.array(coordiante_points,dtype=object)

    return coordiante_points,class_label,sign,object_id






if __name__ == '__main__':
    X_train, y_train, train_sign, train_id = extract_data(sys.argv[1])
    X_test, y_test, test_sign, test_id  = extract_data(sys.argv[2])

    distance_list = []
    match = []

    for i in range(len(X_test)):
        for j in range(len(X_train)):
            series = [X_test[i], X_train[j]]
            distance = dtw.distance_matrix_fast(series, compact = True)
            #print(j, distance[0])
            distance_list.append(distance[0])

        #print(i, distance_list)
        #print("\n\n")
        match.append([k for k, l in enumerate(distance_list) if l == min(distance_list)])
        print(distance_list.index(min(distance_list)))
        distance_list.clear()
        

    print(match)

    #print(match)
