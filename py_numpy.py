import numpy as np  #importing numpy package as np

import time   #importing time module

import sys    #importing sys module

import matplotlib.pyplot as plt    #import matplotlib for data visualization



s = range(1000)  #defining a list

print('Memory taken by list:', sys.getsizeof(5)*len(s))   #getting size taken by list

d = np.arange(1000)

print('Memory taken by numpy array: ',d.size*d.itemsize) #getting size taken by numpy array

size = 1000000

list1 = range(size) #creating list
list2 = range(size) #creating list

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()

list_result = [(x,y) for x,y in zip(list1,list2)] #adding list1 and list2

print('Time taken in adding two list',(time.time()-start)*1000) #measuring time taken to adding to list

start2 = time.time()

numpy_result = a1 + a2

print('Time taken in adding two numpy array',(time.time()-start2)*1000) #measuring time taken to adding to numpy_array


#numpy functions

a = np.array([(1,2,3),(4,5,6)])

print('This is a',a.ndim,'dimension array.') #telling dimensions of array

print('every item taking',a.itemsize,'bytes')   #to know memory occupied by each element

print('The array is',a.dtype)  #to know the data type

print('The array has',a.size,'element')    #find size of array

print('Shape of array is',a.shape)  #for find shape

b = np.array([(1,2,3,4,5,6,7),(3,5,3,5,3,6,7)])

print(b.shape)

print('Reshape result of array',b.reshape(7,2)) #reshaping the array

print('accessing all rows and 4th column',b[0:,4])    #accessing array's element

c = np.linspace(1,3,5) #this line means 5 values between 1 to 3
print('linespacing',c)

d = np.array([1,2,3])

print('Greatest number in array',d.max()) #getting maximum value from array

print('Getting sum of all element of array',d.sum())

e = np.array([(1,2,3),(3,4,5)])

f = np.array([(1,2,3),(3,4,5)])


print('Sum of axis',e.sum(axis=0)) #getting the sum of axis

print('Squre root of each element of the array', np.sqrt(a))    #find the squre root of each element

print('Standred diviation of the array', np.std(a))    #Standred diviation of the array

#you can also perform +,-,*,/ operation of an array


print('Vertical Stacking',np.vstack((e,f)))       #vartical stacking

print('Horizental Stacking', np.hstack((e,f)))    #horizental stacking

print('Merge',e.ravel())   #merge an array


#ploting sin graph
t = np.arange(0,3*np.pi,0.1)

u = np.sin(t)

plt.plot(t,u)
plt.show()

#you can plot graph of tan,cos and other trignometry functionls

#log functions
ad = np.array([1,2,3])

print('Log value of array',np.log10(ad))