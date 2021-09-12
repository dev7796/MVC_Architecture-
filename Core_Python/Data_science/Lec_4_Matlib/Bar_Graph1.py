import numpy as np
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))#it gets the value 0 to len-1
performance = [10,8,6,4,2,1]
print('y_pos>>>>>',y_pos)

plt.bar(y_pos, performance)
plt.xticks(y_pos, objects) # we can assign to the numericals a lable on x axis
plt.xlabel('Programming language')
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()