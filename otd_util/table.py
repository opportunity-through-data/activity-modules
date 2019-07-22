import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize_table(d):
    df = pd.DataFrame(d)
    print(df)

def scatter(d, x, y):
    df = pd.DataFrame(d)
    plt.scatter(d[x], d[y])
    plt.title(x + ' vs. ' + y)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

def line(d, x, y):
    df = pd.DataFrame(d)
    plt.plot(d[x], d[y])
    plt.title(x + ' vs. ' + y)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

def bar(d, x, y):
    df = pd.DataFrame(d)
    plt.bar(d[x], d[y])
    plt.title(x + ' vs. ' + y)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()
