#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Amelia Roseto & Gwyneth Casey & Gabriella Nutt
# Student ID: 2289652
# Email: roseto@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW08
###
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib as plt

def s(t, n, T=2*np.pi):
    """function for summation Sn(t)"""
    k = np.arange(1,n+1)
    k = np.divide(4,np.pi*(2*k-1))
    Sums = np.divide(2*np.pi*(2*np.arange(1,n+1)-1),T) #defining Sn(t)
    answer = np.sum(k*np.sin(Sums*t))
    return answer

def s(t,n,T=2*np.pi):
    """function for summation Sn(t)"""
    k = np.arange(1,n+1)
    a = 4/(np.pi)
    sums = a*((1/(2k-1))*np.sin(((2*(2k-1)*np.pi*t))/T)) #defining Sn(t)
    return np.sum(sums)

def vecs(t,n,T=2*np.pi):
    """Function for vectorizing t"""
    @np.vectorize #decoratot that actually vectorizes t
    def f(t):
        return s(t,n,T)
    return f(t) #bam t is now a vector... magic

def F(t, T=(2*np.pi)):
=======
def F(t, n, T=(2*np.pi)):
   '''t = test variable
   T = domain demonstrating variable'''
   if (t > 0) and (t < T/2):
       return 1
   elif (t < 0) and (t > -T/2):
       return -1
   elif (t == 0):
       return 0
   else:
       print('t is not in domain')
   print(s((np.pi),1000,(2*np.pi)))