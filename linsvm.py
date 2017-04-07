import gradientdescent as gd
import numpy as np
import pickle
import os

def loss(X, Y, w, l, N, p):
    loss = 0
    correct = 0
    truePositive = 0
    falsePositive = 0
    trueNegative = 0
    falseNegative = 0
    for i in range(0, N):
        guess = w.T  * X[i,:].T
        modGuess = -1
        if guess >= 0:
            modGuess = 1
        if modGuess == int(Y[i,:]):
            correct = correct + 1
            if modGuess == 1:
                truePositive += 1
            else:
                trueNegative += 1
        else:
            if modGuess == 1:
                falsePositive += 1
            else:
                falseNegative += 1
        hingeCalc = float(guess * Y[i,:])
        if hingeCalc < 1:
            loss = loss + 1 - hingeCalc
    if p == 1:
        print('Classification rate: ' + str(correct * 1.0 / N))
        print('Positive share: ' + str(truePositive + falseNegative * 1.0 / N))
        print('Negative share: ' + str(trueNegative + falsePositive * 1.0 / N))
        print('Positive accuracy: ' + str(truePositive * 1.0 / (truePositive + falseNegative)))
        print('False accuracy: ' + str(trueNegative * 1.0 / (trueNegative + falsePositive)))
    return (1.0 / N) * loss + l / 2.0 * w.T * w 

def gradient(X, Y, w, eta, l, N):
    gradientSum = 0
    for i in range(0, N):
        hingeCalc = float(w.T * X[i,:].T * Y[i,:])
        if hingeCalc < 1:
            gradientSum += -X[i,:].T * Y[i,:]
    return w - eta * ((1.0 / N) * gradientSum + l * w)

#lambda_values = [1e-11, 1e-12, 1e-13, 1e-14, 1e-15, 1e-16]
#eta_values = [1e-11, 1e-12, 1e-13, 1e-14, 1e-15, 1e-16]

eta_values = [1e-1]
lambda_values = [1e-1]

gd.run_experiment(loss, gradient, eta_values, lambda_values)

