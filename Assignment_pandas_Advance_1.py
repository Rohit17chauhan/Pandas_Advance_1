#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Q1. List any five functions of the pandas library with execution."""


# In[2]:


import pandas as pd


# In[3]:


pip install pandas


# In[4]:


df=pd.read_csv("C:\\Users\\Rohit\\OneDrive\\Desktop\\data.csv")


# In[5]:


df


# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


df.describe()


# In[9]:


df["new_col"]='0'


# In[10]:


df


# In[11]:


df[['Item_MRP']].mean


# In[12]:


"""Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
DataFrame with a new index that starts from 1 and increments by 2 for each row."""


# In[13]:


import pandas as pd

def reindex_dataframe_with_increment(df):
    # Reset the index to the default integer index
    df = df.reset_index(drop=True)

    # Create a new index that starts from 1 and increments by 2
    new_index = range(1, 2 * len(df) + 1, 2)

    # Assign the new index to the DataFrame
    df.index = new_index

    return df

# Example usage:
data = {'A': [10, 20, 30], 'B': [40, 50, 60], 'C': [70, 80, 90]}
df = pd.DataFrame(data)
new_df = reindex_dataframe_with_increment(df)
print(new_df)


# In[14]:


"""Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
function should print the sum to the console."""


# In[15]:


data={"value":[1,2,3]}


# In[16]:


d=pd.DataFrame(data)


# In[17]:


d


# In[18]:


d.sum()


# In[19]:


"""Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
'Word_Count' that contains the number of words in each row of the 'Text' column."""


# In[20]:


t={"Text":["0","0","0"]}


# In[21]:


y=pd.DataFrame(t)


# In[22]:


y


# In[23]:


y["Word_Count"]="Text"


# In[24]:


y


# In[25]:


"""Q5. How are DataFrame.size() and DataFrame.shape() different?"""


# In[26]:


Ans="DataFrame.shape()  is an attribute that returns a tuple containing the number of rows and columns in the DataFrame,DataFrame.size() is an attribute that returns the total number of elements (cells) in the DataFrame, which is equal to the product of the number of rows and columns."


# In[27]:


Ans


# In[28]:


"""Q6. Which function of pandas do we use to read an excel file?"""


# In[29]:


Ans6="pd.read.excel(filename)"


# In[30]:


Ans6


# In[31]:


"""Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email
addresses in the format 'username@domain.com'. Write a Python function that creates a new column
'Username' in df that contains only the username part of each email address."""


# In[32]:


f={"Email":["username@domain.com","username@domain.com"]}


# In[33]:


df=pd.DataFrame(f)


# In[34]:


df["Username"]="Username"


# In[35]:


df


# In[36]:


"""Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
function should return a new DataFrame that contains only the selected rows."""


# In[37]:


import pandas as pd
def select_row(df):
    select_row=df[(df['A']>5) & (df['B']<10)]
    return select_row
data={'A':[2,8,3,6,9],
      'B':[5,2,9,3,1],
      'C':[1,7,4,5,2]}
df=pd.DataFrame(data)
selected_df=select_row(df)
print(selected_df)
    
    
    


# In[38]:


"""Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,
median, and standard deviation of the values in the 'Values' column."""


# In[40]:


import pandas as pd
data={'Values':[12,34,5,6,2]}
df=pd.DataFrame(data)
print(df)


# In[41]:


df.mean()


# In[42]:


df.median()


# In[43]:


df.std()


# In[44]:


"""Q10. Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to
create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days
for each row in the DataFrame. The moving average should be calculated using a window of size 7 and
should include the current day."""


# In[45]:


import pandas as pd

def calculate_moving_average(df):
    df['MovingAverage'] = df['Sales'].rolling(window=7, min_periods=1).mean()
    return df


data = {'Date': pd.date_range(start='2023-11-03', periods=10, freq='D'),
        'Sales': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
df = pd.DataFrame(data)

df = calculate_moving_average(df)
print(df)


# In[46]:


"""Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new
column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.
Monday, Tuesday) corresponding to each date in the 'Date' column."""


# In[48]:


import pandas as pd
def add_weekday(df):
    df['Weakdays']=df['Date'].dt.strftime('A')
    return df
data = {'Date': pd.date_range(start='2023-11-03', periods=5, freq='D')}
df = pd.DataFrame(data)

df = add_weekday_column(df)
print(df)


# In[49]:


"""Q12. Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python
function to select all rows where the date is between '2023-01-01' and '2023-01-31'."""


# In[51]:


import pandas as pd

def select_rows_between_dates(df, start_date, end_date):
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    selected_rows = df[mask]
    return selected_rows

# Example usage:
data = {'Date': pd.date_range(start='2023-01-01', periods=10, freq='D')}
df = pd.DataFrame(data)

start_date = '2023-01-01'
end_date = '2023-01-31'

selected_df = select_rows_between_dates(df, start_date, end_date)
print(selected_df)


# In[50]:


"""Q13. To use the basic functions of pandas, what is the first and foremost necessary library that needs to
be imported?"""


# In[53]:


"To use the basic functions of Pandas, the first and foremost library that needs to be imported is, of course, Pandas itself. You can import Pandas by using the following import statement:import pandas as pdThe common convention is to import Pandas and alias it as pd for easier and more concise usage in your code. Once you have imported Pandas, you can access and use all of its functions and data structures, such as DataFrames and Series, for data manipulation, analysis, and more."


# In[ ]:




