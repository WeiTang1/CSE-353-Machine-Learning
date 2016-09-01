My approach to Naive Bayes Classifier:

I create a big hash map of probabilities.

my top level table is called table

table = {"attribute name":class_table}

level 2 table is called class_table:

class_table = {"label name": (label distribution over >50K, label distribution over <=50K)}  * the Value is a tuple*

for continuous values the class_table would have 2 key value pairs:

class_table = 	{
				"Yes": (mean of the continuous attribute over >50K, standard deviation of it)
				"No": (mean of the continuous attribute over <=50K, standard deviation of it)
				}

Important method:

def normaldis(x,mean,sd) : calculate normal distribution given x, mean and standard deviation

def extract_data(file): extract the data to array 

def get_info(data,continuous_attribute,attribute_index):
the method will go through all the data and make array of attribute labels if its continuous add an empty array

def splitdata(data): split the data with target attribtue

def count_p(data: it will calculate the frequency of target attribtue

def build(trainning_data): it will build the probability table given training data

def test(trainning_data, testing_data): it will make prediction for all entry in testing data based on the probability table generate using testing_data


For Accuracy, please see Report.pdf