# this file is used for testing purpose
import math
import utils
import training

train_labels = 'traininglabels.txt'
train_images = 'trainingimages.txt'
test_labels = 'testlabels.txt'
test_images = 'testimages.txt'

def test_im(im_num_start, im_num_end):
    # after training this function will predict the values on test images in a specific range
    global train_images
    global train_labels
    global test_images
    # get trained values
    p_list, probs = training.training(train_labels,train_images)
    test_result = [] # test_result will store the prediction of test images
    for i in xrange(im_num_start, im_num_end + 1):
        im = utils.read_image(i,test_images)
        prob_v = [0,0,0,0,0,0,0,0,0,0] # prob_v stored the prob. for each value vj
        for j in xrange(10):
            p_a_v = 0
            for k in xrange(28):
                for l in xrange(28):
                    # work with sums of log probabilities rather than products of probabilities to avoid underflow errors
                    if im[k][l] == 0:
                        p_a_v = p_a_v + math.log10(probs[j][k][l][0])
                        if p_a_v == 0:
                            print 'problem'
                    else:
                        p_a_v = p_a_v + math.log10(probs[j][k][l][1])
                        if p_a_v == 0:
                            print 'problem'
            prob_v[j] = math.log10(p_list[j]) + p_a_v
        predict = prob_v.index(max(prob_v))
        test_result.append(predict)
    return test_result

def test(start, end):
    global test_labels
    result = test_im(start, end)
    print "TEST LABEL RESULTS: "
    print result
    test_labels = utils.read_label(test_labels)
    count_labels = [0,0,0,0,0,0,0,0,0,0] # keep track of how many of each values in the label file
    for value in test_labels:
        count_labels[value] = count_labels[value] + 1
    acc = 0
    acc_list =[0,0,0,0,0,0,0,0,0,0]
    for i in xrange(len(result)):
        if result[i] == test_labels[i]:
            acc = acc + 1
            acc_list[test_labels[i]] = acc_list[test_labels[i]] + 1
    acc_percent = (acc/(len(result) * 1.0)) * 100
    for i in xrange(10):
        acc_list[i] = (acc_list[i]/(count_labels[i] * 1.0)) * 100
    print "Digits Accuracy"
    for i in xrange(len(acc_list)):
        print 'Digit ' + str(i) + ': ' + str (acc_list[i])
    print "Average Accuracy: " + str(acc_percent)
test(0,999)