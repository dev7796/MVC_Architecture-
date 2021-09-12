import matplotlib.pyplot as plt
import numpy as np

print(np.arange(1, 5, 1))
print(np.exp((np.arange(1, 5, 1))))


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0.0, 5.0, 0.1)
print(t1)
t2 = np.arange(0.0, 5.0, 0.02)
print(t2)


plt.figure('graph')
plt.subplot(121)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k--')#k is for black

plt.subplot(122)
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
plt.show()
'''subplot(m,n,p) divides the current figure into an m-by-n grid and creates axes in the position specified by p. 
MATLAB® numbers subplot positions by row. The first subplot is the first column of the first row, 
the second subplot is the second column of the first row, and so on. If axes exist in the specified position, 
then this command makes the axes the current axes.'''

'''plt.subplot(2,2,1)
x = np.linspace(0,10);
y1 = np.sin(x);
plt.plot(x,y1)
plt.title('Subplot 1: sin(x)')

plt.subplot(2,2,2)
y2 = np.sin(2*x);
plt.plot(x,y2)
plt.title('Subplot 2: sin(2x)')

plt.subplot(2,2,3)
y3 = np.sin(4*x);
plt.plot(x,y3)
plt.title('Subplot 3: sin(4x)')

plt.subplot(2,2,4)
y4 = np.sin(8*x);
plt.plot(x,y4)
plt.title('Subplot 4: sin(8x)')
plt.show()
'''
#(2,2,_) it means that two rows and two columns and poistions assignedcan be a total of 4