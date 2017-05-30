import csv
import random
import math
import copy
 
# For loading the dataset
def loadData(filename):
	dataset = list()
	with open(filename,'r') as filen:
		data_reader = csv.reader(filen)
		for row in data_reader:
			if not row:
				continue
			dataset.append(row)
		dataset.pop(0)
	# print (dataset[0])
	# print (dataset[109])
	return dataset	


def calcDist (row1,row2):
	dist = 0.0
	for i in range(0,len(row1)):
		dist += (int(row1[i])-int(row2[i])) * (int(row1[i])-int(row2[i]))
	return math.sqrt(dist)


def calcClusterCenter(listVar,dataset):
	# print ("List1 = ",listVar)
	# print ("List1length = ",len(listVar))
	meanList = list()
	for i in zip(*dataset):
		list1 = listVar[:]
		# list1=listVar 
		# Don't use this, it just copies the reference to the list and not the actual list
		# print ("After entereing listVar = ",listVar)
		# print ("After entering list1 = ",list1)
		mean = 0.0
		countCC = 0
		# print ()
		#print ("i = ",i)
		# print ()
		temp = list1.pop(0)
		count2 = 0
		# print ("list1 = ",list1,"  list1.length = ",len(list1))
		# print ("list1.pop = ",list1.pop(0))
		# print ("list1 = ",list1,"  list1.length = ",len(list1))
		for j in i:
			# print ("j = ",int(j))
			# print ("count = ",count)
			if (temp==countCC):
				# print ("Entered2 !!")
				mean += int(j)
				# print ("list1 = ",list1)
				if list1:
					# print ("Entered !!")
					temp = list1.pop(0)
				count2 += 1
			countCC += 1
		# print ("total = ",mean,"  count = ",count2)
		mean = mean/count2
		#print ("count2 = ",count2," listVar length = ",len(listVar))
		meanList.append(mean)
		# print ("mean ",mean)
	# print ("meanList = ",meanList)
	# print ("Length of mean list = ",len(meanList))
	return meanList

def selectRows(dataset,clusterCenter1,clusterCenter2):
	selectedRows = list()

	for i in range(0,len(dataset)):
		distances = list()
		distances.append(calcDist(dataset[i],clusterCenter1))
		distances.append(calcDist(dataset[i],clusterCenter2))
		# print ("Distances = ",distances)
		# fitnessValues.index(max(fitnessValues))
		# selectedRows.append(distances.index(min(distances)))
		if (distances.index(min(distances))==0):
			selectedRows.append(clusterCenter1)
		else:
			selectedRows.append(clusterCenter2)
	return selectedRows

def selectRowsIndex(dataset,clusterCenter1,clusterCenter2):
	selectedRowsIndex = list()

	for i in range(0,len(dataset)):
		distances = list()
		distances.append(calcDist(dataset[i],clusterCenter1))
		distances.append(calcDist(dataset[i],clusterCenter2))
		# print ("Distances = ",distances)
		# fitnessValues.index(max(fitnessValues))
		# selectedRows.append(distances.index(min(distances)))
		if (distances.index(min(distances))==0):
			selectedRowsIndex.append(1)
		else:
			selectedRowsIndex.append(2)
	return selectedRowsIndex

def calcAccuracy (clusters):
	aSelect = list()
	bSelect = list()
	for i in range(0,len(clusters)):
		if (clusters[i]==1):
			aSelect.append(i)
		else:
			bSelect.append(i)
	# print ("In cluster 1 : ",aSelect)
	# print ("In cluster 2 : ",bSelect)
	labels = loadData("Labels.csv")
	# print ("Length of labels = ",len(labels))
	# print ("Labels = ",labels)

	aSelect0 = 0
	aSelect1 = 0
	bSelect0 = 0
	bSelect1 = 0
	for i in aSelect:
		if (int(labels[i][0])==0):
			aSelect0 += 1
		else:
			aSelect1 += 1
	for i in bSelect:
		if (int(labels[i][0])==0):
			bSelect0 += 1
		else:
			bSelect1 += 1
	# print ("Sum = ",aSelect0+aSelect1+bSelect0+bSelect1)
	classOfC1 = 0
	classOfC2 = 0
	if (aSelect0>aSelect1):
		tn = aSelect0
		fn = aSelect1
		classOfC1 = 0
	else:
		tp = aSelect1
		fp = aSelect0
		classOfC1 = 1
	if (bSelect0>bSelect1):
		tn = bSelect0
		fn = bSelect1
		classOfC2 = 0
	else:
		tp = bSelect1
		fp = bSelect0
		classOfC2 = 1
	print ("aSelect0 = ",aSelect0,"  aSelect1 = ",aSelect1)
	print ("bSelect0 = ",bSelect0,"  bSelect1 = ",bSelect1)
	print ("Class of C1 = ",classOfC1)
	print ("Class of C2 = ",classOfC2)

	print ("tp = ",tp)
	print ("tn = ",tn)
	print ("fp = ",fp)
	print ("fn = ",fn)

	# Accuracy
	accuracy = (tp + tn)*1.0/(tp+fp+tn+fn)
	print ("Accuracy = ",accuracy*100)

	# Precision positive
	prePos = (tp)*1.0/tp+fp

	# Precision negative
	preNeg = (tn)*1.0/tn+fn

	# Recall positive
	recPos = (tp)*1.0/tp+fn

	# Recall negative
	recNeg = (tn)*1.0/tn+fp

	print ("Precision + = ",prePos)
	print ("Precision - = ",preNeg)
	print ("Recall + = ",recPos)
	print ("Recall - = ",recNeg)


def kmeans(dataset,clusterCenter1,clusterCenter2,count):

	count += 1
	'''for row in dataset:
		# Defining a list of cluster centers
		clusterCenters = []
		for i in range(0,k):
			clusterCenters.append(random.randint(0,len(row)))
		# print (clusterCenters)'''
	# print ("Length of dataset = ",len(dataset))
	
	# print ("Cluster centers = ",clusterCenters)
	selectedRows = selectRows(dataset,clusterCenter1,clusterCenter2)
	# print ()
	# print ("Selected Centers :")
	# print (selectedCenters)
	# print ()

	'''a = selectedCenters[0]
	b = 0.0
	for i in range(1,len(selectedCenters)):
		if (selectedCenters[i]!=a):
			b = selectedCenters[i]
			break;

	print ("a = ",a,"  b = ",b)'''

	a = clusterCenter1
	b = clusterCenter2
	# print ("a = ",a,"  b = ",b)

	aSelect = list()
	bSelect = list()
	for i in range(0,len(selectedRows)):
		if (selectedRows[i]==a):
			aSelect.append(i)
		else:
			bSelect.append(i)
	# print ("aSelect = ",aSelect)
	# print ("bSelect = ",bSelect)

	oldCC1 = clusterCenter1
	oldCC2 = clusterCenter2
	# print ()
	# print ()
	# print ("oldCC1 = ",oldCC1)
	# print ()
	# print ("oldCC2 = ",oldCC2)
	# print ()
	# print ("Length of oldCC1 = ",len(oldCC1))
	# print ("Length of oldCC2 = ",len(oldCC2))
	# print ()

	newCC1 = calcClusterCenter(aSelect,dataset)
	newCC2 = calcClusterCenter(bSelect,dataset)
	# print ()
	# print ()
	# print ("newCC1 = ",newCC1)
	# print ()
	# print ("newCC2 = ",newCC2)
	# print ()
	# print ("Length of newCC1 = ",len(newCC1))
	# print ("Length of newCC2 = ",len(newCC2))
	# print ()

	distOldNew1 = calcDist(oldCC1,newCC1)
	distOldNew2 = calcDist(oldCC2,newCC2)
	# print ()
	# print ()
	# print ("distOldNew1 = ",distOldNew1)
	# print ()
	# print ("distOldNew2 = ",distOldNew2)
	# print ()

	if (distOldNew1==0 and distOldNew2==0):
		print ("count = ",count)
		clusters = selectRowsIndex(dataset,clusterCenter1,clusterCenter2)
		print ("Clusters ",clusters)
		calcAccuracy(clusters)
		return
	else:
		kmeans(dataset,newCC1,newCC2,count)


def main():

	'''Check for list1.pop(0) error'''

	filename = "SPECTF_New.csv"
	dataset = loadData(filename)
	# k = Number of clusters
	k = 2 
	clusterCentersIndex = []
	for i in range (0,k):
		clusterCentersIndex.append(random.randint(0,len(dataset)))

	# print ("*********** ",)
	clusterCenter1 = []
	clusterCenter2 = []
	clusterCenter1 = dataset[clusterCentersIndex[0]][:]
	clusterCenter2 = dataset[clusterCentersIndex[1]][:]
	
	# print ("clusterCenter1 = ",clusterCenter1)
	# print ("clusterCenter2 = ",clusterCenter2)
	# print ("Length of clusterCenter1 = ",len(clusterCenter1))
	# print ("Length of clusterCenter2 = ",len(clusterCenter2))

	count = 0
	kmeans(dataset,clusterCenter1,clusterCenter2,count)
	# print ("count = ",count)

main()