import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)
#The seed() method is used to initialize the random number generator.
# The random number generator needs a number to start with (a seed value),
# to be able to generate a random number. By default the random number generator uses the current system time.

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)#will generate an array of random 10000 values
print(x)

# the histogram of the data
# n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
n, bins, patches = plt.hist(x, 5, normed=1) #bins = number of bars,
#The last return value of hist is a list of patches, which corresponds to the rectangles with their properties
#Rectangle(xy=(0.676583, 0), width=0.735046, height=1694, angle=0)
#n decides the height of the histogram

#n: is the number of counts in each bin of the histogram
#bins: is the left hand edge of each bin
#patches: is the individual patches used to create the histogram, e.g a collection of rectangles
#The patches can be used to change the properties of individual bars as in these examples.
print(n,bins,patches)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.05])#axis([xmin, xmax, ymin, ymax])
plt.grid(True)
plt.show()

#If you use the same seed to initialize, then the random output will remain the same.