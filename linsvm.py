import gradientdescent as gd
import numpy as np
import pickle
import os

def loss(X, Y, w, l, N):
    h = float(w.T * X.T * Y)
    if 1 > h:
        return (1.0 / N) * (1 - h) + (l / 2) * w.T * w
    else:
        return (l / 2) * w.T * w

def gradient(X, Y, w, eta, l, N):
    h = float(w.T * X.T * Y)
    if 1 > h:
        return w - eta * ( (1.0 / N) * (-X.T * Y) + l * w ) 
    elif 1 < h:
        return w - eta * (l * w) 
    else:
        print ('gradient undefined')
        return -1

#lambda_values = [.1, .01, .001, .0001, .00001, .000001, .0000001]
#eta_values = [.1, .01, .001, .0001, .00001, .000001, .0000001, .00000001]

eta_values = [.0001]
lambda_values = [.0000001]

gd.run_experiment(loss, gradient, eta_values, lambda_values)

