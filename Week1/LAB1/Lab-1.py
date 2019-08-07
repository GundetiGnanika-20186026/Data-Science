#!/usr/bin/env python
# coding: utf-8

# # LAB-1 

# In[3]:



# In this case we're just using % symbol for telling the plotting library to draw things on
# the notebook, instead of on a separate window.
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np # imports a fast numerical programming library
import scipy as sp #imports stats functions, amongst other things
import matplotlib as mpl # this actually imports matplotlib
import matplotlib.cm as cm #allows us easy access to colormaps
import matplotlib.pyplot as plt #sets up plotting under plt
import pandas as pd #lets us handle data as dataframes
#sets up pandas table display
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)
import seaborn as sns #sets up styles and gives us more plotting options


# In[4]:


df=pd.read_csv("all.csv", header=None,
               names=["rating", 'review_count', 'isbn', 'booktype','author_url', 'year', 'genre_urls', 'dir','rating_count', 'name'],
)
df.head()


# In[5]:


df.dtypes #we will get all the types of data in the data frame


# In[6]:


df.shape #6000 rows times 10 columns


# In[7]:


df.shape[0], df.shape[1] #we are accessing the members of the tuple i.e rows and columns seperately


# In[8]:


df.shape[0] #we will get the total number of rows


# In[9]:


df.columns #These are the column names present in the data frame


# In[10]:


type(df.rating) #we will get the type of rating attribute in the data frame


# In[11]:


type(df) #type of data frame


# In[12]:


df.rating < 3 #this is a condition so we will get either true or false 


# In[13]:


np.sum(df.rating < 3) #this is counting all trues and give how many trues are present(this does it by considering 1 as true and 0 as false)


# In[14]:


np.sum(df.rating < 3)/df.shape[0] #we are doing average here df.shape[0] gives us the total number of rows in the dataframe 4/6000 is generally 0.something but as it is a python we will get 0.even if we use 4//6000 this does not work 
#I have got the result as it is python version 3 this wont be in the case of python 2


# In[15]:


np.mean(df.rating < 3.0)


# In[16]:


(df.rating < 3).mean() #we can also calculate the mean in this way


# # Filtering

# In[17]:


df.query("rating > 4.5")


# In[18]:


df[df.year < 0] #we can also filter in this way


# In[19]:


df[(df.year < 0) & (df.rating > 4)] # we can also  combine the conditions in this way


# # Cleaning

# In[20]:


df.dtypes #We first check the datatypes. Notice that review_count, rating_count are of type object (which means they are either strings or Pandas couldnt figure what they are), while year is a float


# In[21]:


df['rating_count']=df.rating_count.astype(int)  #we are trying to fix them by changing their datatypes we may get the error if we have null or Nan values
df['review_count']=df.review_count.astype(int)
df['year']=df.year.astype(int)


# In[22]:


df[df.year.isnull()] #we got the error above because of null values so we are checking whether the null values are present in the year column in the dataframe


# In[ ]:


# we got the values it means we have the null values so we have to delete those null present rows in the data frame


# In[23]:


df = df[df.year.notnull()] #here we are taking the values into df only if the values are not null


# In[ ]:


#now the number of rows should decrease as we have not taken some of the rows as null values are present in them


# In[24]:


df.shape


# In[ ]:


#We removed those 7 rows. Lets try the type conversion again


# In[28]:


df['rating_count']=df.rating_count.astype(int)
df['review_count']=df.review_count.astype(int)
df['year']=df.year.astype(int)


# In[29]:


df.dtypes  #now the data is clean as we have changed the data types


# In[30]:


df.rating.hist(); #Pandas has handy built in visualization.


# In[40]:


sns.set_context("notebook")
meanrat=df.rating.mean()
print (meanrat, np.mean(df.rating), df.rating.median())
with sns.axes_style("whitegrid"): #for getting the graph in a white grid
    df.rating.hist(bins=30, alpha=0.4);# bins = 30 i.e 6x5 grid ,alpha is the opacity(thickness) of the graph
    plt.axvline(meanrat, 0, 0.75, color='r', label='Mean') #vertical line at mean value
    plt.xlabel("average rating of book")
    plt.ylabel("Counts")
    plt.title("Ratings Histogram")
    plt.legend()
       #sns.despine()


# In[41]:


df.review_count.hist(bins=np.arange(0, 40000, 400))


# In[42]:


df.review_count.hist(bins=100)
plt.xscale("log");


# In[43]:


plt.scatter(df.year, df.rating, lw=0, alpha=.08)
plt.xlim([1900,2010])
plt.xlabel("Year")
plt.ylabel("Rating")


# In[44]:


alist=[1,2,3,4,5]


# In[45]:


asquaredlist=[i*i for i in alist]
asquaredlist


# In[46]:


plt.scatter(alist, asquaredlist);


# In[48]:


print (type(alist))


# In[49]:


plt.hist(df.rating_count.values, bins=100, alpha=0.5);


# In[51]:


print (type(df.rating_count), type(df.rating_count.values))


# In[52]:


alist + alist


# In[53]:


np.array(alist)


# In[54]:


np.array(alist)+np.array(alist)


# In[55]:


np.array(alist)**2


# In[56]:


newlist=[]
for item in alist:
    newlist.append(item+item)
newlist


# In[58]:


a=np.array([1,2,3,4,5])
print (type(a))
b=np.array([1,2,3,4,5])

print (a*b)


# In[59]:


a+1


# In[ ]:




