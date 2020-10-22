import numpy as np
from dtaidistance import dtw
import sys
from fastdtw import fastdtw

"""

In this program we will be calculating the DTW distance and finding the best
results with accuracy

"""

###First step is to read in the file :

def extract_data(filename):
    """
    This function will help us extract all the data from the file

    input: filename ( Along with its realtive path)

    output: coordiante_points ( which contains all the actual data/co-ordinate points)
            class_label ( This are the actual classes of each object)
            sign ( What the sign means for that particualr class-label )
            object_id ( What is the unique identification number, also given in file )

    """
    data =  []
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
    This fuction will allow us to calculate simple accuracy % of our model

    input: x ( array 1)
           y ( array 2)


    """
    accuracy_list = []
    for i in range(len(x)):
        if int(x[i]) == int(y[i]):
            accuracy_list.append(1)
        else:
            accuracy_list.append(0)
    accuracy_list = np.array(accuracy_list)
    return np.sum(accuracy_list)/len(accuracy_list)


def main(train_file,test_file):
    """
    This function helps us to calcuate out DTW distance for each test set.
    We take in each test object and find the DTW distance with each train object
    and find the class_label of the train object with the lowest distance and store
    it in our output.txt file

    input: train_file , test_file

    output: we call the accuracy function which then prints out the accuracy on
    the screen

    """
    X_train, y_train, train_sign, train_id = extract_data(train_file)
    X_test, y_test, test_sign, test_id  = extract_data(test_file)
    distance_list = []
    match = []
    with open("output.txt", "a") as f:
        for i in range(len(X_test)):
            for j in range(len(X_train)):
                distance,_ = fastdtw(X_test[i],X_train[j])
                distance_list.append(distance)
            if y_train[distance_list.index(min(distance_list))] == y_test[i]:
                acc = 1
            else:
                acc = 0
            f.write("ID=%5s, predicted=%3s, true=%3s, accuracy=%4.2s, distance = %.2s\n"%(test_id[i], y_train[distance_list.index(min(distance_list))], y_test[i], acc, distance))
            match.append(y_train[distance_list.index(min(distance_list))])

            distance_list.clear()

    match = np.asarray(match,dtype=np.int)

    return accuracy(match,y_test)*100
