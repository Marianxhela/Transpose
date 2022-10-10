#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
import numpy as np
import openpyxl


# In[ ]:


#Read excel file

data = pd.read_excel(r'C:\Users\m.lila\Desktop\Treasury.xlsx', sheet_name='Cash Flow', header = None)
print(data)


# In[ ]:


# Create a dataframe from excel

df = pd.DataFrame(data)
df = df.iloc[7:]
df


# In[ ]:


# Transpose the dataframe

new_data = df.T  

df.dropna(axis = 1, how="all", inplace= True)
df.dropna(axis = 0, how='all', inplace= True)

new_data


# In[ ]:


with pd.ExcelWriter(r'C:\Users\m.lila\Desktop\Treasury.xlsx', mode="a",if_sheet_exists='replace',engine="openpyxl") as writer:

    df.T.to_excel(writer, sheet_name="Optimised Cash Flow") 

