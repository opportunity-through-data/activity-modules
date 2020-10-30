import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_table(file, columns=None, column_names=None):
    if columns:
        df = pd.read_csv(file, usecols=columns)
        if column_names:
            return df.rename(columns=column_names)
        return df
    return pd.read_csv(file)

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
    plt.xticks(rotation=45)
    plt.ylabel(y)
    plt.show()

def histogram(d, label, bins=None):
    assert not bins or type(bins) == int, "If bins is provided, it should be an integer."
    df = pd.DataFrame(d)
    plt.hist(d[label])
    plt.xlabel(label)
    plt.ylabel("Frequency")
    plt.show()

