def extract_data(file):
	data = []
	for line in open(file):
		line = line.strip()
		entry = line.split('\t')
		if "?" not in entry:
			data.append(line.split('\t'))
	return data


trainning_data = extract_data("cse353-hw3-data.tsv")
