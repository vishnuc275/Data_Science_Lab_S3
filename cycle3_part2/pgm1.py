#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
iris=pd.read_csv("iris.csv")
print("shape of dataset= ",iris.shape)
print("")
print("first and last five rows : ")
print(iris.head)
print(" ")
print("size : ",iris.size)
print(" ")
print(" ")
print("no of samples available for each variety : ", iris["variety"].value_counts())
print(" ")
print(" ")
print(iris.describe())




# In[25]:


sns.pairplot(iris, hue="variety", kind="hist")
print(" ")
print(" ")
print(" ")
sns.pairplot(iris, hue="variety", kind="scatter")
print(" ")
print(" ")
print(" ")
sns.pairplot(iris, hue="variety", kind="kde")
print(" ")
print(" ")
print(" ")
sns.pairplot(iris, hue="variety", kind="reg")


# In[33]:


sns.displot(data=iris)


# In[30]:


sns.histplot(data=iris)


# In[31]:


sns.relplot(data=iris)


# In[ ]:




