import numpy as np
action = np.random.randint(low=0,high=5,size=1)
#print(type(action))
#print(action[0])
test = np.array([[[0,2,3,4],[1,5,9,3],[2,3,99,4]],[[0,2,3,4],[1,5,9,3],[2,3,99,4]]])
te = np.array([[0,2,3,4],[1,5,9,3],[2,3,99,4]])
print(test.shape)
#print(np.max(test,axis=1))
#print(np.sum(test))
#print(np.sum(te))
x = np.array([[[0,2,np.nan,4],[1,5,9,3],[2,3,99,4]],[[0,2,3,4],[1,5,9,3],[2,np.nan,99,4]]])
x = x[np.logical_not(np.isnan(x))]
print(x.shape)
print(x)