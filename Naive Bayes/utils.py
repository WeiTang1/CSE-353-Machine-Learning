def read_image(num_im, file):
    # this function will read the training images file and return a specific
    # image as a 28x28 matrix determine by the num_in. num_in is the order
    # of the image in training dataset starting with 0.
    fp = open(file)
    im = []
    for i, line in enumerate(fp):
        if i >= (num_im * 28) and i < (num_im * 28) + 28:
            # remove newline character at the end of the line
            line = line[:28]
            bin_line = [] # bin_line stores the line as list of 0 and 1
            for c in line:
                if c == ' ':
                    bin_line.append(0)
                else:
                    bin_line.append(1)
            im.append(bin_line)
    fp.close()
    return im

def read_label(file):
    # this function will read the training labels and return the results as a list
    fp = open(file)
    labels = []
    for line in fp:
        labels.append((int)(line.rstrip('\n')))
    return labels