#!/usr/bin/env python
# coding: utf-8

# # Sprial Matrix
# __The Code should receive an x by y matrix and print out the spiral form of the matrix. Outside edges first, then inwards and clockwise.__

# In[20]:


import numpy as np
import math


# _For a Python matrix I used the Numpy library and created a Numpy array_

# In[26]:


my_array = np.array([[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]])


# In[27]:


type(my_array)


# In[28]:


print(my_array)


# In[29]:


def spiral_matrix(spiral):
    
    rows, cols = spiral.shape
    
    start_row = 0
    start_col = 0

    end_row = rows - 1
    end_col = cols - 1

    total = rows*cols
    count = 0

    while count < total:

        for j in range(start_col, end_col, 1):
            print(spiral[start_row][j])
            count += 1
            if count == total:
                break
                    
        if count == total:
                break
        
        for i in range(start_row, end_row, 1):
            print(spiral[i][end_col])
            count += 1
            if count == total:
                break
        
        if count == total:
            break

        for j in range(end_col, start_col, -1):
            print(spiral[end_row][j])
            count += 1
            if count == total:
                break
        
        if count == total:
            break

        for i in range(end_row, start_row, -1):
            print(spiral[i][start_col])
            count += 1
            if count == total:
                break
        
        if count == total:
            break

        start_row += 1
        start_col += 1
        end_row += -1
        end_col += -1


# In[30]:


spiral_matrix(my_array)


# In[ ]:




