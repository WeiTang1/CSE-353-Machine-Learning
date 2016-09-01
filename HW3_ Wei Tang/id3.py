# Wei Tang

import math
#hard coded attribute index
attribute_indexs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
#continuous attributes index
continuous_attribute_indexs = [0,2,4,10,11,12]
target_attribute_index = 14
target_attribute_value = ">50K"


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


def extract_data(file):
    # read from file to extract data entry
    # if an data entry has "?" discard it
    # return an array of entry 
    data = []
    for line in open(file):
        line = line.strip()
        entry = line.split('\t')
        if '?' not in entry:
            data.append(line.split('\t'))
    return data

# data is array of entry
# entry is an array, for example:
#['38', 'Private', '215646', 'HS-grad', '9', 'Divorced', 'Handlers-cleaners', 'Not-in-family', 'White', 'Male', '0', '0', '40', 'United-States', '<=50K\n']

def get_entropy(data):
    ## get entropy of an given data set
    pos, neg,res = 0.0,0.0,0.0
    for entry in data:
        if entry[target_attribute_index] == target_attribute_value:
            pos = pos+1.0
        else:
            neg = neg +1.0
    # check for boundry case of log(0)
    if pos == 0 :
        pos = len(data)
    if neg == 0:
        neg = len(data)
    res =  (-(neg/len(data)) * math.log(neg/len(data),2))+ (-(pos/len(data)) * math.log(pos/len(data),2))
    return res


def get_best_attribute(data,attribute_index):
    # get the attribute with most infomation gain given the attribute_indexes
    # return a tuple (index of best attribute, continuous variable? True:False, threshold of continuous variable)
    information_gains = []
    for index in attribute_index:
        information_gains.append(get_information_gain(data,index))
    index_of_best_attribute = attribute_indexs[information_gains.index(max(information_gains,  key = lambda x:x[0]))]
    if index_of_best_attribute in continuous_attribute_indexs:
        return index_of_best_attribute, True, max(information_gains,  key = lambda x:x[0])[1]
    else:
        return index_of_best_attribute, False, -1


def majority_classifier(data):
    # return the most frequence classifier withint data
    if len(data) == 0:
        return "<=50K"
    # if accurance of target_attribtue value / len (data ) > 0.5 mean target attribtue value is majority
    count = 0.0
    for entry in data:
        if entry[target_attribute_index] == target_attribute_value:
            count = count + 1
    proportion = count/len(data)
    if proportion >0.5:
        return target_attribute_value
    else:
        return "<=50K"


def get_information_gain(data, attribute_index):
    # return informaiont gain of an attribute
    # handle continuous attribute first
    if attribute_index in continuous_attribute_indexs:
        # tempdata for sortig 
        tempdata = data[:]
        tempdata.sort(key = lambda x:x[attribute_index])
        # array for store all c-value AKA threshold
        candidate = []
        # get all possible c value
        for x in range(1,len(tempdata)):
            if tempdata[x-1][target_attribute_index] != tempdata[x][target_attribute_index]:
                candidate.append((float(tempdata[x-1][attribute_index])+float(tempdata[x][attribute_index]))/2)
        # array for all possible information gains for threshold
        info_gains = {}
        # calculate all possible infomation gains for allthreshold
        for cand in candidate:
            cand_info_gain = 0 
            pos,neg,cand_entropy = 0.0,0.0,0.0
            for entry in data:
                if float(entry[attribute_index]) <= cand:
                    pos = pos + 1
                else:
                    neg = neg + 1 
            left_sub_data, right_sub_data = sub_data_continuous(cand,data,attribute_index)
            if pos == 0:
                pos = len(data)
            if neg == 0:
                neg = len(data)
            else:
                cand_info_gain = get_entropy(data) - pos/len(data) * get_entropy(left_sub_data)- neg/len(data)*get_entropy(right_sub_data)
            info_gains[cand] = cand_info_gain
        c_value =  max(info_gains, key = info_gains.get)
        max_infomation_gain = info_gains[c_value]
        return max_infomation_gain,c_value

        #discrete value
    else:
        # discrete: Gain(S,A) = entropy(s) - sum Sv/S entropy(Sv)
        # value_frequence stores key(entry value) value(apparance time)
        values_frequence = {}
        for entry in data:
            if values_frequence.has_key(entry[attribute_index]):
                values_frequence[entry[attribute_index]] = values_frequence[entry[attribute_index]] +1.0
            else:
                values_frequence[entry[attribute_index]]  = 1.0
        expected_entropy = 0.0
        for value in values_frequence:
            sub_data = sub_data_discrete(value,data,attribute_index)
            expected_entropy = expected_entropy + values_frequence[value]/len(data) *get_entropy(sub_data)

        information_gain = get_entropy(data) - expected_entropy
        return information_gain,-1

def sub_data_continuous(c_value,data,attribute_index):
    #divide data by threshold 
    sub_data_left = []
    sub_data_right = []
    for entry in data:
        if float(entry[attribute_index]) <= c_value:
            sub_data_left.append(entry)
        else:
            sub_data_right.append(entry)
    return sub_data_left,sub_data_right

def sub_data_discrete(value,data,attribute_index):
    # divide data by its value
    sub_data = []
    for entry in data:
        if (entry[attribute_index] == value):
            sub_data.append(entry)
    return sub_data

def maketree(data,attribute_indexs):
    tree = {}
    # base case 1 if no data or no attribute left to make tree
    if len(data)==0 or len(attribute_indexs)==0:
        return majority_classifier(data)
    #base case 2 if all data has the same classifier return the classifier
    same_calssifier = True
    for i in xrange(len(data)-1):
        if data[i][target_attribute_index] != data[i+1][target_attribute_index]:
            same_calssifier = False
    if same_calssifier:
        return (data[0][target_attribute_index])
    # get the best attribute if continuous continuous = True 
    best_attribute , continuous,c_value = get_best_attribute(data,attribute_indexs)
    # remove that attribtue from list
    attribute_indexs.remove(best_attribute)
    # make tree
    tree = {best_attribute:{}}
    # if attribute is continuous make 2 sub trees with one classifer is negative threshold other positive
    if continuous:
        left_data,right_data = sub_data_continuous(c_value,data,best_attribute)
        left_sub_tree = maketree(left_data,attribute_indexs)
        tree[best_attribute][c_value*(-1.0)] = left_sub_tree
        right_sub_tree = maketree(right_data,attribute_indexs)
        tree[best_attribute][c_value] = right_sub_tree
    else:
        # for each value in the attribute make a sub tree
        for value in attribute_values[best_attribute]:
            sub_data = sub_data_discrete(value,data,best_attribute)
            tree[best_attribute][value] = maketree(sub_data,attribute_indexs)

    return tree

def testing(data,tree):
    test_result = []
    correct_predict = 0
    count = 0
    for entry in data:
        temp_tree = tree
        root = False
        # loop would stop if it reach the leaf
        while root == False:
            attribute_index = temp_tree.keys()[0]
            if attribute_index in continuous_attribute_indexs:
                c_value = abs(temp_tree[attribute_index].keys()[0])
                if float(entry[attribute_index])<=c_value:
                    # check if it reaches the leaf node
                    if (temp_tree[attribute_index][c_value*-1] == target_attribute_value) or (temp_tree[attribute_index][c_value*-1]== "<=50K"):
                        prediction =  temp_tree[attribute_index][c_value*-1]
                        if prediction == entry[target_attribute_index]:
                            correct_predict = correct_predict +1
                        count = count+1
                        root = True
                    # if not get in to the next node with its attribute
                    else:
                        temp_tree = temp_tree[attribute_index][c_value*-1]
                else:
                    # same here
                    if (temp_tree[attribute_index][c_value*1] == target_attribute_value) or (temp_tree[attribute_index][c_value*1]== "<=50K"):
                        prediction =  temp_tree[attribute_index][c_value*1]
                        if prediction == entry[target_attribute_index]:
                            correct_predict = correct_predict +1
                        count = count+1
                        root = True
                    else:
                        temp_tree = temp_tree[attribute_index][c_value*1]
            else:
                # discrete attribtues
                if (temp_tree[attribute_index][entry[attribute_index]] == target_attribute_value) or (temp_tree[attribute_index][entry[attribute_index]] == "<=50K"):
                    prediction =  temp_tree[attribute_index][entry[attribute_index]]
                    if prediction == entry[target_attribute_index]:
                        correct_predict = correct_predict +1
                    count = count+1
                    root = True
                else:
                    temp_tree = temp_tree[attribute_index][entry[attribute_index]]    

    return float(correct_predict)/float(len(data))

# divide data in to 5 sub sets
five_fold_data=[]
results=[]
whole_data = extract_data("smalldata.tsv")
attribute_values = get_info(whole_data,continuous_attribute_indexs,attribute_indexs)

slicing_poing = len(whole_data)/5
five_fold_data.append(whole_data[0:slicing_poing])
five_fold_data.append(whole_data[slicing_poing:slicing_poing*2])
five_fold_data.append(whole_data[slicing_poing*2:slicing_poing*3])
five_fold_data.append(whole_data[slicing_poing*3:slicing_poing*4])
five_fold_data.append(whole_data[slicing_poing*4:slicing_poing*5])

for data in five_fold_data:
    testing_data = data
    index = [0,1,2,3,4]
    index.remove(five_fold_data.index(data))
    training_data = []
    tree = {}
    result = 0
    for i in index:
        training_data = training_data + data
    print "Genterate tree: "
    attribute_indexs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
    tree = maketree(training_data,attribute_indexs)
    print tree
    print "Testing result:"
    result = testing(testing_data,tree)
    results.append(result)
    print result
total = 0.0
for re in results:
    total = total+re
print "average",total/5


