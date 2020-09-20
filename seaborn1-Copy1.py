#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


df=sns.load_dataset("tips")


# In[3]:


df.head()


# In[4]:


df.corr()


# In[5]:


sns.heatmap(df.corr())


# In[7]:


#jointplot(study btwn 2 numeric variables usually in hexagonal shape ) univeriate analysis 

sns.jointplot(x='tip',y='total_bill',data=df, kind='hex')


# In[8]:



# its a  scatterplot in which one variable in the same data row is matched with another variable

sns.pairplot(df)


# In[9]:


sns.pairplot(df,hue ='sex')


# In[10]:


sns.pairplot(df,hue='size')


# In[11]:


sns.pairplot(df,hue='smoker')


# In[16]:


sns.pairplot(df,hue='tip')


# In[17]:


# dist plot helps in creating histogram 
sns.distplot(df['tip'])


# In[18]:


#character baised plots 
#count plot
sns.countplot('sex',data=df)


# In[22]:


#barplot
sns.barplot(y ='total_bill', x ='sex', data=df)


# In[25]:


sns.barplot(y ='smoker', x ='total_bill', data=df)


# In[24]:


### box plot 
## box plot  presents  information of data on a 5_number summary form

sns.boxplot('sex','total_bill',data=df)


# In[26]:


sns.boxplot('smoker','total_bill',data=df)


# In[27]:


sns.boxplot(data=df,orient='v')


# In[31]:


sns.boxplot('sex','total_bill', data=df)


# In[32]:


sns.boxplot('sex','total_bill', data=df, palette='rainbow')


# In[33]:


#categorising data on some other category data

sns.boxplot(x='total_bill',y='day',hue='smoker',data=df)


# In[35]:


#violin data

# helps us classify data in terms of both kde(kernal density estimation ) & box plot 

sns.violinplot(x='total_bill',y='day',data=df,palette='rainbow')
   


# In[6]:


## HOME WORK (pratice on this data_set)
 
import seaborn as sns    
iris=sns.load_dataset('iris')


# In[8]:


iris.head()


# In[17]:


iris.boxplot('sepal_length','sepal_width',df=iris)


# In[10]:


iris=sns.load_dataset('iris')


# In[11]:


iris.corr()


# In[21]:


sns.pairplot(iris,hue='petal_width')


# In[ ]:




