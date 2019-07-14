import math
import operator
import random

def euclidean(training_set, row, k):

    euclidean_values = []

    for element in training_set:
        element_euclidean_value = 0
        for key in element.keys():
            if key not in ['class', 'type']:
                element_euclidean_value += (float(element[key]) - float(row[key])) ** 2
        euclidean_values.append((math.sqrt(element_euclidean_value), element['class']))

    euclidean_values.sort()
    ranking = dict()

    for i in range(k):
        key = euclidean_values[i][1]
        if key in ranking:
            ranking[key] = ranking[key] + 1
        else:
            ranking[key] = 1

    sorted_ranking = sorted(ranking.items(), key=operator.itemgetter(1), reverse =  True)
    return sorted_ranking[0][0]


def ibl1_training_set(training_set_base):
    k = len(training_set_base)
    training_set = []

    well = 0
    badly = 0

    if (k > 0):
        training_set.append(training_set_base[0]) #always add first element
        
        #we must random our dataset to avoid sequential same classes registers
        r = range(1,k)
        random.shuffle(r)

        for i in r:
            row = training_set_base[i]
            euclidean_class = euclidean(training_set, row, 1)
            
            if (row['class'] != euclidean_class):
                badly = badly + 1
            else:
                well = well + 1

            #learn everything
            training_set.append(row)

    return {'well' : well,
            'badly': badly,
            'data' : training_set}



def ibl2_training_set(training_set_base):
    k = len(training_set_base)
    training_set = []

    well = 0
    badly = 0

    if (k > 0):
        training_set.append(training_set_base[0]) #always add first element
        
        #we must random our dataset to avoid sequential same classes registers
        r = range(1,k)
        random.shuffle(r)

        for i in r:
            row = training_set_base[i]
            euclidean_class = euclidean(training_set, row, 1)
            
            #learn just what is not well classified
            if (row['class'] != euclidean_class):
                training_set.append(row)
                badly = badly + 1
            else:
                well = well + 1

    return {'well' : well,
            'badly': badly,
            'data' : training_set}

def test(training_set, width, height, k, step):
    w = range (0, width, step)
    h = range (0, height, step)

    random.shuffle(w)
    random.shuffle(h)

    data = []
    for i in w:
        for j in h:
            row = {'x': i, 
                   'y': j}
            euclidean_class = euclidean(training_set, row, k)
            row['class'] = euclidean_class
            data.append(row)

    return data
