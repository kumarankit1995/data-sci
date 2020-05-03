import numpy as np

# Create an array with values ranging from 12 to 38

a = np.arange(12,38,1)
print(a)

# Add a border around an existing array
b =np.ones((3,3))
print(np.pad(b,1,constant_values=0))

# Convert a list and tuple into arrays
c = np.arange(1,9).reshape(2,4)
d = np.asarray(c).reshape(2,4)
print(c)
print(d)

# Convert the values of Centigrade degrees into Fahrenheit degrees

e= np.array([0.,12.,45.21,34.,99.91])
e= (e-32)*(5/9)
print(e)

# Write a NumPy program to find the number of elements of an array,
# length of one array element in bytes and total bytes consumed by the elements

f = np.arange(3)
print('Size of the array is :',f.size)
print('Length of one item is :',f.itemsize)
print('Total bytes consumed by the element is :',f.size * f.itemsize)

# Get the unique elements of an array

g = np.array([10,10,20,20,30,30])
h = np.array([[1,1],[2,2]])
print(np.unique(g))
print(np.unique(h))

# Change the dimension of an array

i = np.arange(1,10,1)
print(i.reshape(3,3))

# Create a 1-D array of 30 evenly spaced elements between 2.5. and 6.5, inclusive

j = np.linspace(2.5,6.5,30)
print(j)


# Convert 1-D arrays as columns into a 2-D array

k = np.arange(10,40,10)
l = np.arange(40,70,10)
m = np.row_stack((k,l))
print(m)

# Create a 5x5 matrix with row values ranging from 0 to 4







# Sum of all the multiples of 3 or 5 below 100

n=[]
for i in np.arange(3,100,1):
     if (i%3==0) | (i%5==0):
         n.append(i)
print(n)
print(np.sum(n))

# Combine a one and a two dimensional array together and display their elements

o = np.arange(0,4)
p = np.arange(0,8).reshape(2,4)

for i, j in np.nditer([o,p]):
    print('%d:%d'%(i,j))

# replace all elements of NumPy array that are greater than specified array

q = np.random.rand(2,3)
print(q)
q[q>0.5]=0.5
print(q)


# Add a new row to an empty numpy array

r = np.empty((0,3))
r = np.append(r,np.array([[10,20,30]]),axis=0)
r = np.append(r,np.array([[40,50,60]]),axis=0)
print(r)

# join a sequence of arrays along a new axis

s = np.arange(1,4).reshape(1,3)
t = np.arange(2,5).reshape(1,3)
print(np.row_stack((s,t)))

u = np.arange(1,4).reshape(3,1)
v = np.arange(2,5).reshape(3,1)
print(np.vstack((u,v)))