#!/usr/bin/env python
# coding: utf-8

# In[95]:


import numpy as np

def NBTWs(matrixA,k,v,w):
    deg =np.zeros((len(matrixA),), dtype=int)
    s= 0
    for i in range(len(matrixA)):
        s= 0
        for j in range(len(matrixA)):
            s = s+ matrixA[i][j]
        deg[i]= s
       
    P2 = np.array(np.dot(matrixA,matrixA)-np.diag(deg),dtype = int)
    
   
    if k== 1:
        return matrixA[v][w]
    elif k == 2:
        return P2[v][w]
    else:
        PrOne = P2
        PrTwo = matrixA
        Pr = P2
        for i in range(k-2):
            P2 = Pr
            Pr = np.array(np.dot(matrixA,PrOne)- np.dot(np.diag(deg)-np.identity(len(matrixA)),PrTwo),dtype = int)
            PrTwo = PrOne
            PrOne = Pr
  
    return(Pr[v][w])


# In[97]:


def main():
    n = 6
    k = 8
    matrixA  = np.array(np.ones((n,), dtype=int)-np.identity(n),dtype= int)
    print("Number of NBTWs walks of length",k," is ", NBTWs(matrixA,k,0,0), "between nodes 1 and 1" )
    print("Number of NBTWs walks of length",k," is ", NBTWs(matrixA,k,1,0), "between nodes 1 and 2" )
    
    n = 8
    k = 7
    matrixA  = np.array(np.ones((n,), dtype=int)-np.identity(n),dtype= int)
    print("Number of NBTWs walks of length",k," is ", NBTWs(matrixA,k,0,0), "between nodes 1 and 1" )
    print("Number of NBTWs walks of length",k," is ", NBTWs(matrixA,k,1,0), "between nodes 1 and 2" )
    
    n = 10
    k = 6
    matrixA  = np.array(np.ones((n,), dtype=int)-np.identity(n),dtype= int)
    print("Number of NBTWs walks of length",k," is ", NBTWs(matrixA,k,0,0), "between nodes 1 and 1" )
    print("Number of NBTWs walks of length",k," is ", NBTWs(matrixA,k,1,0), "between nodes 1 and 2" )
   

    
    


# In[98]:


import numpy as np
main()


# In[ ]:




