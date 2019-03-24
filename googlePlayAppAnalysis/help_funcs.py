import math
import numpy as np
from time import time
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def time_it(func):
	"""measure time"""
	start = time()
	func()
	end = time()
	return round(end - start, 3)

def abs_val(prcnt, all_values):
	"""return absolute value by given precent and whole column"""
	val = np.sum(all_values) * prcnt / 100
	return '{p:.2f}%\n({v:.0f})'.format(p=prcnt,v=val)


def proceed_func(series, steps = 50):
	"""launch value_counts on given series a lot of times"""
	for i in range(steps):
		series.value_counts()


def millify(n):
	"""replace bunch of zeroes to either m,k or b"""
	millnames = ['','k','m','b']
	n = float(n)
	millidx = max(0, min(len(millnames)-1, int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
	return '{:.1f}{}'.format(n / 10**(3 * millidx), millnames[millidx])


def bar_chart(heights, bar_title = '', rot = 0):
	"""plot and show bar chart by given height with random bar width and color"""
	# generating random values
	bar_width = np.random.uniform(0.5, 0.9, 1)[0]
	bar_color = np.random.rand(3,)
	# bar_alpha = np.random.uniform(0.5, 1, 1)[0]

	fig,ax = plt.subplots()

	bar_pos = range(len(heights))

	plt.title(bar_title)
	plt.xticks(bar_pos, heights.keys().str.lower(), rotation=rot)
	plt.bar(bar_pos, heights.values, width = bar_width, color = bar_color)
	plt.grid(True)
	ax.set_axisbelow(True)
	number_over_bar_height = heights.max() * 0.01
	plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.0f'))

	for i, height in enumerate(heights.values):
		plt.text(i - bar_width / 4, height + number_over_bar_height, millify(heights.values[i]))
	
	plt.show()
