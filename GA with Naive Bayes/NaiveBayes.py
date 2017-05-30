# Example of Naive Bayes implemented from Scratch in Python
import csv
import random
#from random import randrange
import math
 
# chooseCols is a list containing the column numbers 
# which are to be included in the dataset 
def loadCsv(filename, chooseCols):
    count = 0
    # print("Choosecols = ",chooseCols)
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    # print (dataset)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    newDataset = list(list())
    choose = list()
    for i in range(len(dataset)):
        count += 1
        # print ("i = ",i)
        choose[:]=[]
        for j in chooseCols:
            # print("dataset[i][j] = ",dataset[i][j])
            choose.append(dataset[i][j])
        choose.append(dataset[i][44])
        # print("Choose = ",choose)
        # print(newDataset)
        #print("Appending",choose) 
        newDataset.append(choose[:])
        # if (count <= 2 ):
        #     print("New dataset = ")
        #     print(newDataset)
    # print ("New dataset = ",newDataset)
    return newDataset

'''def loadCsv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset'''
 
def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]
 
def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated
 
def mean(numbers):
    return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)
 
def summarize(dataset):
    summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries
 
def summarizeByClass(dataset):
    separated = separateByClass(dataset)
    summaries = {}
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)
    return summaries
 
def calculateProbability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/float(2*math.pow(stdev,2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
 
def calculateClassProbabilities(summaries, inputVector):
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculateProbability(x, mean, stdev)
    return probabilities
            
def predict(summaries, inputVector):
    probabilities = calculateClassProbabilities(summaries, inputVector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel
 
def getPredictions(summaries, testSet):
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i])
        predictions.append(result)
    return predictions
 
def getAccuracy(testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

# *********************************************** 
def cross_validation_split(dataset,no_folds):
    split = list()
    copy = list(dataset)
    fold_size = int(len(dataset) / no_folds)
    for i in range(no_folds):
        fold = list()
        while(len(fold) < fold_size):
            index = random.randrange(len(copy))
            fold.append(copy.pop(index))
        split.append(fold)
    return split

def calculate(dataset,no_folds):
    folds = cross_validation_split(dataset,no_folds)
    p=1
    accuracies=list()

    for fold in folds:
        #print fold
        #print ("Cross fold validation : ",p)
        p+=1 
        train_data = list(folds)
        train_data.remove(fold)
        #print("Before sum ------ ",train_data);
        train_data = sum(train_data,[])
        #print("After sum --------- ",train_data);
        test_data=list()
        for row in fold:
            r_copy = list(row)
            test_data.append(r_copy)
            #r_copy[0] = None
        summaries = summarizeByClass(train_data)
        #print("Test data : ",test_data)
        # test model
        predictions = getPredictions(summaries, test_data)
        accuracy = getAccuracy(test_data, predictions)
        accuracies.append(accuracy)
        #print('Accuracy : ',accuracy)
    avgAccuracy = sum(accuracies)/float(len(accuracies))
    #print('Avg accuracy : ', avgAccuracy)
    return avgAccuracy
# **************************************************
 
def main(dataset):
    return calculate(dataset,10)
 
# main()