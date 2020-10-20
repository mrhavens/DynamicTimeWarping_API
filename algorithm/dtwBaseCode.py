import numpy as np
from dtaidistance import dtw
import sys
from fastdtw import fastdtw

"""
Impemented DTW code here
"""

###First step is to read in the file :

def extract_data(filename):
    """
    This function will take the raw file and then seperate all the data that are necessary

    input : filename (with relative position)

    outputs: co-ordinate points (actual data points)
             class_label (actual class label list )
             sign (what does that sign mean)
             object_id (ehat ids object id)

    """
    with open(filename) as f:
        file_data = f.read() #read the whole file and save to variable data
        data = (file_data.split('-------------------------------------------------'))
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


def accuracy(x,y):
    """
    This fucntion will find out the accuracy of our model

    input: x (this will be a list of all the predicted output)
           y (actual output)

    output: accuracy

    """
    accuracy_list = []
    for i in range(len(x)):
        #print(x[i], y[i])
        if int(x[i]) == int(y[i]):
            accuracy_list.append(1)

        else:
            accuracy_list.append(0)
    accuracy_list = np.array(accuracy_list)
    print(accuracy_list)
    print("Accuracy = ", np.sum(accuracy_list)/len(accuracy_list))
    return np.mean(accuracy_list)


def main(train_file,test_file):
    X_train, y_train, train_sign, train_id = extract_data(train_file)
    X_test, y_test, test_sign, test_id  = extract_data(test_file)
    distance_list = []
    match = []
    path, dist = dtw_path(X_test[0],X_train[1])
    print(dist)

    for i in range(len(X_test)):
        for j in range(len(X_train)):
            distance,_ = fastdtw(X_test[i],X_train[j])
            print(distance)
            distance_list.append(distance)
        match.append(y_train[distance_list.index(min(distance_list))])

        distance_list.clear()


    #print(y_test)
    match = np.asarray(match,dtype=np.int)

    return accuracy(match,y_test)*100
