import NaiveBayes
import random

# x=NaiveBayes.main()
# print(x)

def initializeChromosomes(populationSize, chromosomeLength):
	c=list()
	# print("Chrom length = ",chromosomeLength)
	for i in range (0, populationSize):
		c.append(list())
		for j in range (0, chromosomeLength):
			c[i].append(random.randint(0,1))
	# print (c)
	return c

# chromosomes = population (which is 30 in number)
def fitnessEvaluation(chromosomes,fileName):
	choose = list()
	flag = 0
	count = 0
	fitnessValues=list()
	# print("Chromosomes = ", chromosomes)
	for row in chromosomes:
		count += 1
		choose[:]=[]
		# print(row)
		for j in range(0,len(row)):
			# print(row[j], end='')
			if (row[j]==1):
				choose.append(j)
		# print("Choose : ", choose)
		# print()
		dataset = NaiveBayes.loadCsv(fileName,choose)
		# if (flag==0):
		# 	print (dataset)
		# 	flag=1
		# x is the fitness function value
		# print ("dataset = ",dataset)
		x = NaiveBayes.main(dataset)
		fitnessValues.append(x)
		# print ("count = ",count,"  x = ",x)
	return fitnessValues

def rouletteWheel(chromosomes,fileName):
	fitnessValues = fitnessEvaluation(chromosomes,fileName)
	#print ("Fitness values = ",fitnessValues)
	total = sum(fitnessValues)
	print ("Max fitness value = ",max(fitnessValues)," Chromosome = ",chromosomes[fitnessValues.index(max(fitnessValues))])
	# Calculating probabilities of individual elements
	probabilities = list()
	for i in fitnessValues:
		probabilities.append(i/total)
	# print("Probabilities = ",probabilities)
	# print("Length of probabilities = ",len(probabilities))

	# Calculating cumulative probabilities
	cumulative = list()
	sumCum = 0.0
	for i in probabilities:
		sumCum += i
		cumulative.append(sumCum)
	# print ("Cumulative probabilities = ",cumulative)
	# print ("Length of cumulative probabilities = ",len(cumulative))

	# Generating random numbers between 0 and 1
	randList = list()
	# print ("Length of chromosomes = ",len(chromosomes))
	for i in range(0, len(chromosomes)):
		randList.append(random.uniform(0, 1))
	# print ("Random numbers list = ",randList)
	# print ("Length of random numbers list = ",len(randList))

	# Selecting new chromosomes
	selectedChromosomes = list()
	for i in randList:
		count = 0
		for j in cumulative:
			if (j>i):
				selectedChromosomes.append(count)
				break
			count += 1
	# print ("Selected chromosomes = ",selectedChromosomes)
	# print ("Length of selected chromosomes = ",len(selectedChromosomes))

	# Replacing the chromosomes
	newChromosomes = list()
	for i in selectedChromosomes:
		newChromosomes.append(chromosomes[i])
	# print ("Orignal chromosomes = ",chromosomes)
	# print ("New chromosomes = ",newChromosomes)
	# print ("Length of new chromosomes = ",len(newChromosomes))
	return crossover(chromosomes,newChromosomes)

def crossover (chromosomes,newChromosomes):
	# CROSSOVER
	# Generate 30 (population length) random numbers between 0 and 1
	randListCrossover = list()
	for i in range(0, len(chromosomes)):
		randListCrossover.append(random.uniform(0, 1))
	# print ("Random numbers list = ",randListCrossover)
	# print ("Length of random numbers list = ",len(randListCrossover))

	# Crossover rate
	cr = 0.25

	# Selecting chromosomes for crossover
	selectedCrossover = list()
	count = -1
	for i in randListCrossover:
		count += 1
		if (i<cr):
			selectedCrossover.append(count)
	# print ("Chromosomes slected for crossover = ",selectedCrossover)
	# print ("Length of chromosomes selected for crossover = ",len(selectedCrossover))

	# Initialization of list of chromosomes which will result after crossover
	chromosomesAfterCrossover = list()
	for i in newChromosomes:
		chromosomesAfterCrossover.append(i)
	# print ("chromosomesAfterCrossover = ")
	# for i in range(0,len(chromosomesAfterCrossover)):
		# print ("i = ",i)
		# print (chromosomesAfterCrossover[i])
	# print ("Length of chromosomesAfterCrossover = ",len(chromosomesAfterCrossover))

	for i in range(0, len(selectedCrossover)):
		if (i==(len(selectedCrossover)-1)):
			j = 0
		else:
			j = i+1
		x = random.randint(0,7)
		# print ("x = ",x)
		# print ("i = ",i, " j = ",j)
		# print ("selectedCrossover[i] = ",selectedCrossover[i])
		# print ("selectedCrossover[j] = ",selectedCrossover[j])
		# print (len(chromosomes[0])-8 , " ********* ")
		# for k in range(len(chromosomes)):
		copy = newChromosomes
		for k in range(x,len(chromosomes[0])):
			copy[selectedCrossover[i]][k] = newChromosomes[selectedCrossover[j]][k]
		chromosomesAfterCrossover = copy
	# print ("After crossover : ",chromosomesAfterCrossover)
	# print ("Length after crossover = ",len(chromosomesAfterCrossover))
	return mutation(chromosomesAfterCrossover)

def mutation (chromosomesAfterCrossover):
	# Mutation rate
	mr = 0.10
	# Total number of genes in the population
	numGenes = len(chromosomesAfterCrossover)*len(chromosomesAfterCrossover[0])
	# print ("Total number of genes = ",numGenes)

	# Number of genes to be taken for mutation
	numGenesForMutation = mr * numGenes
	# print ("numGenesForMutation = ",numGenesForMutation)

	# Generating random number list for mutation
	randListMutation = list()
	for i in range(0, int(numGenesForMutation)):
		randListMutation.append(random.randint(0,numGenes-1))
	# print ("Random number list for mutation = ",randListMutation)
	# print ("Length of randomnumber list for mutation = ",len(randListMutation))

	# print ("Before mutation = ",chromosomesAfterCrossover)
	# Mutating the genes
	for i in randListMutation:
		j = int(i/44) # 9 is the chromosome length
		k = i%44
		# print ("i = ",i," j = ",j, " k = ",k)
		if (chromosomesAfterCrossover[j][k]==0):
			chromosomesAfterCrossover[j][k]=1
		elif (chromosomesAfterCrossover[j][k]==1):
			chromosomesAfterCrossover[j][k]=0
	# print ("After mutation = ",chromosomesAfterCrossover)
	# print ("Length of chromosomes after mutation = ",len(chromosomesAfterCrossover))
	return chromosomesAfterCrossover

def main():
	# Number of chromosomes = population size = 30
	popuSize = 30
	# Chromosome length = Total attributes - 1
	chromLength = 44
	fileName = "SPECTF_New.csv"
	# dataset = NaiveBayes.loadCsv(fileName)
	# print (dataset)
	chromosomes = initializeChromosomes(popuSize,chromLength)
	# print(len(chromosomes))
	# print(len(chromosomes[0]))
	# print(len(chromosomes[18]))
	# print(chromosomes)
	for i in range (0,25):
		print ("i = ", i)
		chromosomes = rouletteWheel(chromosomes,fileName)
		

main()
