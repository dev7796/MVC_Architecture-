import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 4
means_frank = (90, 55, 40, 65)
means_guido = (85, 62, 54, 20)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_frank, bar_width,
alpha=opacity,
color='b',
label='Frank')

rects2 = plt.bar(index+bar_width, means_guido, bar_width,
alpha=opacity,
color='g',
label='Guido')

plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index, ('A', 'B', 'C', 'D'))
plt.legend()# Automatic detection of elements to be shown in the legend
#loc : str or pair of floats, default: rcParams["legend.loc"] = 'best'
# ('best' for axes, 'upper right' for figures)

plt.tight_layout(pad=5,h_pad=11)#Automatically adjust subplot parameters to give specified padding.
#tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)
plt.show()