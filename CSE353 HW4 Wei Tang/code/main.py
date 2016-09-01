import math
# attribute class name
attribute_class = ["age",
"workclass",
"fnlwgt",
"education",
"education-num",
"marital-status",
"occupation",
"relationship",
"race",
"sex",
"capital-gain",
"capital-loss",
"hours-per-week",
"native-country"]
target_attribute_index = 14
target_attribute_value = ">50K"
# index of continuous attributes 
continuous_attribute_indexs = [0,2,4,10,11,12]
attribute_indexs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

#calculate normal distribution given mean and standard deviation
def normaldis(x, mean, sd):
    pi = 3.1415926
    denom = (2*pi)**.5 * sd
    num = math.exp(-(x-mean)**2/(2*(sd**2)))
    return num/denom
# take data from file get rid of entry with "?"
def extract_data(file):
	data = []
	for line in open(file):
		line = line.strip()
		entry = line.split('\t')
		if "?" not in entry:
			data.append(line.split('\t'))
	return data

def get_info(data,continuous_attribute_indexs,attribute_indexs):
    # get some basic idea about the data:
    # returns an array with the same attribute indexs but store all value of discrete attributes and an empty array for continuous attribute

    attribute_values = []
    for index in attribute_indexs:
        if index in continuous_attribute_indexs:
            attribute_values.append([])
        else:
            value_array = []
            for entry in data:
                if entry[index] not in value_array:
                    value_array.append(entry[index])
            attribute_values.append(value_array)
    return attribute_values

#split the data in half with target attribute
def splitdata(data):
	yes = []
	no = []
	for entry in data:
		if entry[target_attribute_index] == target_attribute_value:
			yes.append(entry)
		else:
			no.append(entry)
	return yes,no

# count the probability distribution of target attribute ">50K" : Yes "<=50K": No
def count_P(trainning_data):
	# get P(>50) and p (<50)
	P_Yes = 0.0
	P_No = 0.0
	for entry in trainning_data:
		if entry[target_attribute_index] == target_attribute_value:
			P_Yes = P_Yes +1.0
		else:
			P_No = P_No +1.0
	return P_Yes,P_No

# funtion for build probability table
def build(trainning_data):
	table={}
	yes_data,no_data = splitdata(trainning_data)
	P_Yes,P_No=count_P(trainning_data)
	discrete_labels = get_info(trainning_data,continuous_attribute_indexs,attribute_indexs)

	for i in attribute_indexs:
	# in entry[i]:
	# if it is continuous:
	    if i in continuous_attribute_indexs:
	    	# calculate the mean and standard deviation of the attribute
	        class_table = {}
	        yes_total = 0.0
	        no_total = 0.0
	        for temp in yes_data:
	            yes_total = yes_total + int(temp[i])
	        for temp in no_data:
	        	no_total = no_total + int(temp[i])

	        yes_mean = yes_total/len(yes_data)
	        no_mean = no_total/len(no_data)

	        yes_stDev = 0.0
	        for temp in yes_data:
	        	# get the sum of square
	        	yes_stDev = yes_stDev+ ( int(temp[i]) - yes_mean )**2

	        yes_stDev =math.sqrt( yes_stDev/(len(yes_data)-1))

	        no_stDev = 0.0
	        for temp in no_data:
	        	# get the sum of square
	        	no_stDev = no_stDev+ ( int(temp[i]) - no_mean )**2

	        no_stDev = math.sqrt(no_stDev/(len(no_data)-1))
	        # creat a dictionary with Key "Yes" Value: tuple(mean for yes, standard dev for yes)
	        class_table["Yes"] = (yes_mean,yes_stDev)
	        class_table["No"] = (no_mean,no_stDev)

	        table[attribute_class[i]] = class_table
	    else:
	    	# descrite attribute
	        class_table = {}
	        for label in discrete_labels[i]:
	        	# notice that i initialize it to 1.0 for all to avoid 0 probability
	            yes,no = 1.0,1.0
	            for temp in yes_data:
	                if temp[i] == label:
	                    yes = yes+1
	            for temp in no_data:
	                if temp[i] == label:
	                    no = no +1
	            # create a dictionary entry with label as key and it's frequency as a tuple
	            class_table[label] = (yes/P_Yes,no/P_No)

	    table[attribute_class[i]] = class_table
	return table



# function for testing
def testing(testing_data,trainning_data):
	# build probability table with trainning data
	table = build(trainning_data)
	print table,'\n'
	# counter for correct prediction
	correct= 0.0
	# make prediction
	for entry in testing_data:
		likelihood_yes,likelihood_no = count_P(trainning_data)
		#initializa likelihood with the probability of the target attribute
		likelihood_yes = likelihood_yes/len(trainning_data)
		likelihood_no = likelihood_no/len(trainning_data)
		for i in attribute_indexs:
			# continuous variable
			if i in continuous_attribute_indexs:
				# calculate the normal distribution of the attribute
				likelihood_yes = likelihood_yes * normaldis(float(entry[i]),table[attribute_class[i]]["Yes"][0], table[attribute_class[i]]["Yes"][1])   
				likelihood_no = likelihood_no * normaldis(float(entry[i]),table[attribute_class[i]]["No"][0], table[attribute_class[i]]["No"][1]) 
			else:
				# handle discrete class
				likelihood_yes = likelihood_yes * table[attribute_class[i]][entry[i]][0]
				likelihood_no = likelihood_no * table[attribute_class[i]][entry[i]][1]
		# normalize the distribution
		prediction_yes = likelihood_yes/(likelihood_yes+likelihood_no)
		prediction_no = likelihood_no/(likelihood_yes+likelihood_no)
		# make prediction
		prediction = ""
		if (prediction_yes>prediction_no):
			prediction = target_attribute_value
		else:
			prediction = "<=50K"
		if prediction == entry[target_attribute_index]:
			correct = correct +1.0

	accuracy = correct/len(testing_data) *100
	return accuracy

#extract data and make probability table:
whole = "cse353-hw2-data.tsv"
test = "test.tsv"

five_fold_data=[]

whole_data = extract_data(whole)

# slicing the data
slicing_poing = len(whole_data)/5
five_fold_data.append(whole_data[0:slicing_poing])
five_fold_data.append(whole_data[slicing_poing:slicing_poing*2])
five_fold_data.append(whole_data[slicing_poing*2:slicing_poing*3])
five_fold_data.append(whole_data[slicing_poing*3:slicing_poing*4])
five_fold_data.append(whole_data[slicing_poing*4:slicing_poing*5])
result = []
# five fold test
for data in five_fold_data:
    testing_data = data
    index = [0,1,2,3,4]
    index.remove(five_fold_data.index(data))
    training_data = []
    tree = {}
    for i in index:
        training_data = training_data + data
    result.append(testing(testing_data,training_data))
sum = 0.0
for i in range(0,5):
	print "Accuracy of fold number: ",i+1," ",result[i],"%"
	sum = sum +result[i]

print "Average accuracr: ", sum/5 ,"%"












