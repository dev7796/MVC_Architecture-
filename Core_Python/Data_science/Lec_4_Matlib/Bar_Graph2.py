import numpy as np
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.barh(y_pos, performance, align='edge', alpha=0.9)#alpha decides intensity of the colour
plt.yticks(y_pos, objects)
plt.xlabel('Usage')
plt.title('Programming language usage')

plt.show()

#{‘center’, ‘edge’}, optional, default: ‘center’
#If ‘center’, interpret the x argument as the coordinates of the centers of the bars.
# If ‘edge’, aligns bars by their left edges
#To align the bars on the right edge pass a negative width and align='edge'