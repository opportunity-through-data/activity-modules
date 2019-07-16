import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Utils:
	def visualize_table(d):
		df = pd.DataFrame(d)
		print(df)

	def scatter(d, x, y):
		df = pd.DataFrame(d)
		plt.scatter(d[x], d[y])

	def line(d, x, y):
		df = pd.DataFrame(d)
		plt.plot(d[x], d[y])

	def bar(d, x, y):
		df = pd.DataFrame(d)
		plt.bar(d[x], d[y])
