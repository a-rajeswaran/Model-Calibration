# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:38:40 2024

@author: a-raj
"""

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

def Newton(f,x, eps=0.001, nmax=1000, h=0.001):
    compteur = 0
    while abs(f(x))>eps and compteur < nmax:
        df = (f(x+h) - f(x))/h
        x = x - f(x)/df
        compteur +=1
    print(compteur)
    return x

def Newton2(f, x, y, eps=0.001, nmax=1000, h=0.001):
    compteur = 0
    while abs(f(x,y))>eps and compteur < nmax:
        dfx = (f(x+h, y) - f(x,y))/h
        x = x - f(x,y)/dfx
        dfy = (f(x, y+h) - f(x,y))/h
        y = y - f(x,y)/dfy
        compteur +=1
    print(compteur)
    return x,y
    

def f1(x):
    return np.exp(x) -2
def f2(x):
    return 2 + x**3
def f3(x):
    return np.log(x)
def f4(x):
    return np.arctan(x) - 2*np.cos(np.cos(x) - 1) 
def f5(x):
    return 1 - np.exp(-(x**2))
def f6(x):
    return np.sqrt(abs(x))
def f7(x,y):
    return y*(x**2) +2
def f8(x,y):
    return np.log(1 + (x**2 + y**2 - 1)**2)
def f9(x,y,n):
    return 20 + np.exp(1) - 20*np.exp(-0.2*np.sqrt((x**2+y**2)/n)) - np.exp((np.cos(np.pi*2*x) + np.cos(np.pi*2*y))/n)
    
T=1
S=100
r=0
K=120
def BS(vol):
    d1 = (np.log(S/K) + (r+(vol**2)/2)*T )/(np.sqrt(T)*vol)
    d2 = d1 - np.sqrt(T)*vol
    N1 = scipy.stats.norm.cdf(d1)
    N2 = scipy.stats.norm.cdf(d2)
    return N1 - N2*K*np.exp(-r*T)


C_market = 2.74
def diff(vol):
    return (BS(vol) - C_market)

vol = Newton(diff, 0.1)
print(vol)

    
    
    
        
    
    






        
        