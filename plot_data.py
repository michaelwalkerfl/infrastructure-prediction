#!/usr/bin/python

import matplotlib.pyplot as plt
import scipy as sp
from sys import argv

data = sp.genfromtxt("data/%s" % argv[1], delimiter="\t")

x = data[:,0]
y = data[:,1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

def plot(data):
    plt.scatter(x,y)
    plt.title("Web traffic over the last month")
    plt.xlabel("Time")
    plt.ylabel("Hits/hour")
    plt.xticks([w*30*24 for w in range(10)],
     ['week %i'%w for w in range(10)])
    plt.autoscale(tight=True)
    plt.grid()
    plt.show()


if __name__ == '__main__':
	plot(data)


