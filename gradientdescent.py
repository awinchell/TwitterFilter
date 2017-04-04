import numpy as np
import os
import os.path
import pickle
import matplotlib.pyplot as plt

import setup as s 

(training_X, training_Y, test_X, test_Y) = s.run()

training_N, num_features = training_X.shape
test_N, num_features2 = test_X.shape

def train_increment(gradient, w, eta, l):
    return gradient(training_X, training_Y, w, eta, l, training_N)

def train(gradient, T, eta, l):
    w = np.zeros((num_features,1))
    for t in range(0, T):
        w = train_increment(gradient, w, eta, l) 

    return w

def train_err(loss, w, l):
    return float(loss(training_X, training_Y, w, l, training_N))
'''
def val_err(loss, w, l):
    return float(loss(val_X, val_Y, w, l, val_N))
'''
def test_err(loss, w, l):
    return float(loss(test_X, test_Y, w, l, test_N))

def run_experiment(loss, gradient, eta_values, lambda_values):
    T = 1000
    best_combo = (0, 0) 
    lowest_err = float("inf")
    
    for l in lambda_values:
        for eta in eta_values:
            w = train(gradient, T, eta, l)
            
            tr_err = train_err(loss, w, l)
            #v_err = val_err(loss, w, l)
            #t_err = test_err(loss, w, l)

            print "eta: " + str(eta)
            print "lambda: " + str(l)
            print "training error: " + str(tr_err)
            #print "validation error: " + str(v_err)
            #print "test error: " + str(t_err)
            print
            '''
            if v_err < lowest_err:
                best_combo = (eta, l)
                lowest_err = v_err
            '''
            if tr_err < lowest_err:
                best_combo = (eta, l)
                lowest_err = tr_err

    best_T = 0 
    lowest_err = float("inf")

    max_T = 1000

    T_values = range(1, max_T + 1)
    err_values = [] 

    w = np.zeros((num_features,1))

    best_eta = best_combo[0]
    best_lambda = best_combo[1]

    for T in T_values:
        w = train_increment(gradient, w, best_eta, best_lambda)
        
        #err = val_err(loss, w, l)
        #err = test_err(loss, w, 1)
        err = train_err(loss, w, l)

        err_values.append(err)

        if err < lowest_err:
            best_T = T
            lowest_err = err
    

    w = train(gradient, best_T, best_eta, best_lambda)
    
    print "best T: " + str(best_T)
    print "best eta: " + str(best_eta)
    print "best lambda: " + str(best_lambda)
    print "test error: " + str(test_err(loss, w, l))
    
    plt.plot(T_values, err_values, '-')

    #  plt.ylim([1e-20, 1])

    plt.title('Training Error vs. T Values')
    plt.xlabel('T Value')
    plt.ylabel('Training Error')

    plt.show()
    
