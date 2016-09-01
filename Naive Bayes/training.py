import utils

def training(label_file, image_file):
    # this function used to train data from training datasets and will
    # return list of P(vj), matrix of P(ai,j = 1|vj), and matrix of P(ai,j = 0|vj)
    # smooth_type determines which type of smoothing data used. There are 2 that will be used in this hw:
    #   +
    #   +

    # first compute the list of P(vj) from the training labels dataset,
    # which is the list of size 10 stores P(0),P(1),...,P(9) in that order
    label_list = utils.read_label(label_file)
    p_list = [0,0,0,0,0,0,0,0,0,0]
    count_p_list = [0,0,0,0,0,0,0,0,0,0] # this list will count the number of images corresponding to each label
    for e in label_list:
        p_list[e] = p_list[e] + 1
        count_p_list[e] = count_p_list[e] + 1
    for i in xrange(len(p_list)):
        p_list[i] = p_list[i]/5000.0

    # compute P(ai,j = 1|vj) and P(ai,j = 0|vj)
    probs = [[],[],[],[],[],[],[],[],[],[]]
    for i in xrange(5000):
        # read each image
        curr_im = utils.read_image(i, image_file)
        label = label_list[i]
        if len(probs[label]) == 0:
            # create and initialize 28x28 matrix
            for row in curr_im:
                prob_row = []
                for j in row:
                    prob_tuple = [0,0]
                    if j == 0:
                        prob_tuple[0] = prob_tuple[0] + 1
                    else:
                        prob_tuple[1] = prob_tuple[1] + 1
                    prob_row.append(prob_tuple)
                probs[label].append(prob_row)
        else:
            # add to current matrice
            for row in xrange(28):
                for col in xrange(28):
                    if curr_im[row][col] == 0:
                        probs[label][row][col][0] = probs[label][row][col][0] + 1
                    else:
                        probs[label][row][col][1] = probs[label][row][col][1] + 1
    # divide each element in probs by # of count corresponding vj to get the prob.
    # Using Laplace Smoothing with k = 1
    for i in xrange(10):
        for j in xrange(28):
            for k in xrange(28):
                probs[i][j][k][0] = (probs[i][j][k][0] + 1)/(count_p_list[i] * 1.0 + 2.0)
                probs[i][j][k][1] = (probs[i][j][k][1] + 1)/(count_p_list[i] * 1.0 + 2.0)
    return p_list, probs



