#!/usr/bin/env python
# coding: utf-8

# # A/B Testing Example
# 
# We will now run through the steps in A/B testing through an example. Consider the following scenario: Cal, a student at UC Berkeley, is signing up for classes and gets to decide between taking his Data Science class in the morning or in the afternoon. He has heard from some students that students in the afternoon class get better grades on their finals. Cal wants to determine whether there is truly a difference between the distributions of students in the morning classes and the afternoon classes, or whether this difference he observed was due to the people he talked to (random chance).

# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')

from datascience import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# ### Data:
# Cal has randomly asked students in the morning class and the afternoon class about their grade on the final. He collected this data in a table called classes. 

# In[2]:


classes = Table.read_table('classesdata.csv')
classes


# In[3]:


classes.group('Time', np.average)


# In[19]:


classes.hist('Score', group='Time')


# ## 1. Formulate hypotheses.

# Null hypothesis:
# 
# Alternative hypothesis:

# ## 2. Define test statistic.

# Test statistic = avg afternoon grade - avg morning grade

# ## 3. Calculate observed value of the test statistic.

# In[5]:


means_table = ...
means_table


# In[6]:


observed_stat = ...
observed_stat


# ## 4. Simulate test statistic under the null hypothesis.

# In[7]:


## Shuffle the labels

shuffled = ...
tbl_w_shuffled = ...
tbl_w_shuffled


# In[8]:


## Calculate the test statistic with these shuffled labels
shuffled_tbl = ...
shuffled_group_means = ...
shuffled_group_means


# In[9]:


## Create a function to do this process many times

def calculate_test_stat(tbl, label, group_label):
    ...
    return ...


# In[10]:


calculate_test_stat(classes, 'Score', 'Time')


# In[11]:


## How can we do this process many times and store the simulated test stat each time?
## This will help us to understand the variance of the test statistic

diffs = ...

...


diffs


# ## 5. Make a conclusion.

# In[15]:


## Plot the distribution of the simulated test statistics.

Table().with_column('Difference Between Group Means', diffs).hist()
plt.title('Prediction Under the Null Hypothesis');


# In[20]:


## Calculate the p-value

p_val = ...
p_val


# In[ ]:




