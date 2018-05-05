# Bisection Solving
# Kobe Arthur Scofield
# 2018-05-04
# Build 2
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.7

import numpy as np

def selffunc(x):
    """
    Put your function below
    """
    return (2 * np.sin(x * np.pi) + np.cos(x * np.pi))
#

a = float(input("Input a: "))
b = float(input("Input b: "))
sigma = float(input("Input epsilon: "))
k = 0

# Core: Core fixed
while True:
    if not(selffunc(a)*selffunc(b) > 0):
        if (selffunc(a)*selffunc(b) == 0):
            if (selffunc(a) == 0):
                rzt = a
                break
            else:
                rzt = b
                break
        else:
            m = (a + b) / 2
            if (np.abs(a - b) < sigma):
                rzt = m
                break
            else:
                if (selffunc(m) != 0.0):  # V2 Fix
                    if ((selffunc(a)*selffunc(m)) > 0): # Fixed
                        a = m
                    else:
                        b = m
                    k+=1
                else:
                    rzt = m
    else:
        a = float(input("Input a: "))
        b = float(input("Input b: "))
print("Result = %f, k = %f" % (rzt, k))

