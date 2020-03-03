import numpy as np

A=np.array([[11,12,13,14],[15,16,17,18]])

x=np.array([0,1,2,3])
y=np.array([-1,0.2,0.9,2.1])

A = np.vstack([x,np.ones(len(x))]).T
print(A)

At_A = A.T.dot(A)
print(At_A)

At_y = A.T.dot(y)
print(At_y)

from numpy.linalg import solve

c = solve(At_A,At_y)
print(c)
 