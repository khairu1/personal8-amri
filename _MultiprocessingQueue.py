#!/usr/bin/env python
# coding: utf-8

# In[1]:


#   Created by Elshad Karimov on 31/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# How to use multiprocessing.Queue as a FIFO queue:

from multiprocessing import Queue

customQueue = Queue(maxsize= 3)
customQueue.put(1)
print(customQueue.get())


# In[ ]:




