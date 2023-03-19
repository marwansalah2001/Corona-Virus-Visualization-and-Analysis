#!/usr/bin/env python
# coding: utf-8

# # <span style=color:#008000><b>Covid 19 Analysis and Visualization

# ![ ](covid2.jpg)

# In[1]:


import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
import time
get_ipython().run_line_magic('load_ext', 'memory_profiler')
start = time.time()


# # <span style =color:blue>Data abstraction Phase (Three levels) :
# 
# ## 1-identify dataset type, attribute types
# ## 2-identify cardinality
# ## 3-consider whether to transform data

#  
#  
#  

# # 1) <span style =color:blue>First - Data Set Types : <span style=color:Red>Table
# 
# ## I-Data Based On <span style= color:Green>Country Wise</span> (2019)
# ## II-Data Based On <span style= color:Green>World Happiness </span>(2019)

# In[2]:


country_wise = pd.read_csv('Country_wise_latest.csv')
World_happ=pd.read_csv('2019.csv')


# # Samples
#     

# In[3]:


#Printing first 10 rows of the data
country_wise.head()


# In[4]:


#Printing first 10 rows of the data
World_happ.head()


# # <span style=color:blue> Second - Identify attributes Types : 
#     
#   
# ## <span style=color:Green>I) Country Wise:
# 
#   1-<b>Country/Region</b> :<span style=color:red> Categorical</span> (Names of Countries)
# 
#   2-<b>Confirmed</b> : <span style=color:red> Quantitative</span> (Number of Postively Confirmed Cases)
# 
#   3-<b>Deaths</b> : <span style=color:red> Quantitative</span> (Number of Deaths due to Corona)
# 
# 
#   4-<b>Recovered</b> : <span style=color:red> Quantitative</span> (Number of Recovered people)
# 
#   5-<b>Active</b> : <span style=color:red> Quantitative</span> (Number of Active (still infected) people)
# 
#   6-<b>New Cases</b> : <span style=color:red> Quantitative</span> (New Recorded Corona Cases)
#     
#   7-<b>New deaths</b> : <span style=color:red> Quantitative</span> (Number of recently dead people)
#     
#   8-<b>New recovered</b> : <span style=color:red> Quantitative</span> (Number of newely recovered people)
#     
#     
#   9-<b>Confirmed last week</b> : <span style=color:red> Quantitative</span> (Number of Confirmed Cases Last Week from 30/1/2020)
#     
#   10-<b>1 week % increase</b> : <span style=color:red> Quantitative</span> (Percentage of the increasing Cases in one week)
#     
#   11-<b>WHO Region</b> :<span style=color:red> Categorical</span> (Names of continents )
#     
# 
#     

# ## <span style=color:Green> II) World Happiness:
# 
# 1-<b>Overall rank</b> : <span style=color:red> Ordinal</span> (Ranks of countries based on happiness record)
#     
# 2-<b>Country or region</b> : <span style=color:red> Categorical</span> (Countries Names)
#     
# 3-<b>Score</b> : <span style=color:red> Quantitative</span> (A metric measured in 2019 by asking the sampled people the question: "How would you rate your happiness on a scale of 0 to 10 where 10 is the happiest.)
# 
# 4-<b>GDP per capita</b> : <span style=color:red> Quantitative</span> (It is sum of gross value added by all resident producers in the economy plus any product taxes not included in the valuation of output, divided by mid-year population)
# 
# 5-<b>Social support
# </b> : <span style=color:red> Quantitative</span> (Network of family, friends, neighbors, and community members that is available in times of need to give psychological, physical, and financial help)
#     
# 6-<b>Healthy life expectancy</b> : <span style=color:red> Quantitative</span> (The extent to which Life expectancy contributed to the calculation of the Happiness Score)    
#   
# 7-<b>Freedom to make life choices</b> : <span style=color:red> Quantitative</span> (The extent to which Freedom contributed to the calculation of the Happiness Score.)    
#     
# 8-<b>Generosity</b> : <span style=color:red> Quantitative</span> (The extent to which Generosity of country people contributed to the calculation of the Happiness Score.)    
#     
# 9-<b>Perceptions of corruption</b> : <span style=color:red> Quantitative</span> (The extent to which Perception of Corruption contributes to Happiness Score.)   

# # 2) <span style=color:blue>Identify Cardinality
#     
#     - How many rows de we have?
#     - Number of levels of categorical Data?
#     - Range of Quantitative Data?

# ## How Many rows?
# 

# ## <span style=color:green> I) Country Wise

# In[5]:


country_wise.shape


# We have 187 Rows , 12 Columns

# ## <span style=color:green> II) World Happiness

# In[6]:


World_happ.shape


# We have 156 rows , 9 columns

# # Number of levels of categorical Data?

# ## <span style=color:green> I) Country Wise
#     -Country/Region
#     -WHO Region

# In[7]:


country_wise["Country/Region"].nunique()


# In[8]:


country_wise["WHO Region"].nunique()


# We have 187 country and 6 continents

# ## <span style=color:green> II) World Happiness

# In[9]:


World_happ["Country or region"].nunique()


# # Ranges of Quantitative Data

# ## <span style=color:green> I) Country Wise

# In[10]:


country_wise.describe()


# ## <span style=color:green> II) World Happiness

# In[11]:


World_happ.describe()


# # 3) <span style=color:blue>Consider wether transform Data 

# In <span style=color:green> Countr Wise </span> Data we may derive data using "Deaths" , "Confirmed" and "Recovered" Columns for fair evaluation of comparisons between countries in number of deaths , confirmed and recovered cases.
# 
# For example:
# 
# We cannot compare Country as <b>USA</b> with 328.3 million population with <b>Benin</b> that is only 11.8 million
# Solution: Scale number of deaths and recovered cases realtive to Confirmed cases

# # Function to calculate the Deaths/100 cases

# In[12]:


def calc_cols(new_name,col1,col2):
    for i in range (0,187):
        
        country_wise[new_name][i]=round((country_wise[col1][i]/country_wise[col2][i])*100,2)
            
        
    


# In[13]:


#creating empty new columns
country_wise["Deaths/100 Cases"]=0


# In[14]:


calc_cols("Deaths/100 Cases","Deaths","Confirmed")


# In[15]:


country_wise.info()


# In[16]:


country_wise.head()


# In[17]:


country_wise.tail()


# # <span style=color:red> Question 1
# 
# ## Who are our top 15 countries in Postively Confirmed Cases?
# 
#     

# <h2><span style=color:blue> Idiom : <br>
#     
# <span style=color:red>Horizontal Bar Chart</span></span></h2>
#     
# <h2><span style=color:blue> Data </span></h2>
#     
# 
# -Categorical: <span style=color:red> Countries
#     
# -Quantitative: <span style=color:red> Number Of Confirmed
#     
# <h2><span style=color:blue> Task </span></h2>
#     
# 
# <span style=color:red> Compare countries with respect to their Confirmed cases.

# In[18]:


fig = px.bar(country_wise.sort_values("Confirmed").tail(15), 
                 x="Confirmed", y="Country/Region", color='WHO Region',  
                 text="Confirmed", orientation='h', width=700, 
                 color_discrete_sequence = px.colors.qualitative.Dark2)
fig.update_layout(title="Top 15 Countries with Confirmed cases", xaxis_title="Confirmed", yaxis_title="Country", 
                      yaxis_categoryorder = 'total ascending',
                      uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()


# <span style=color:Green> - USA,Brazil and Russia are leading our plot with the highest Confirmed Cases 
#     
#  <span style=color:Green>- There are 7 <b>European Countries</b> out of 15 country

# # <span style=color:red> Question 2
# 
# ## Now let's see Who are our top 15 countries in number of Deaths recorded overall
# 
#     

# <h2><span style=color:blue> Idiom : <br>
#     
# <span style=color:red>Horizontal Bar Chart</span></span></h2>
#     
# <h2><span style=color:blue> Data </span></h2>
#     
# 
# -Categorical: <span style=color:red> Countries
#     
# -Quantitative: <span style=color:red> Number Of Deaths
#     
# <h2><span style=color:blue> Task </span></h2>
#     
# 
# <span style=color:red> Compare countries with respect to their Deaths.

# In[19]:


fig = px.bar(country_wise.sort_values("Deaths").tail(15), 
                 x="Deaths", y="Country/Region", color='WHO Region',  
                 text="Deaths", orientation='h', width=700, 
                 color_discrete_sequence = px.colors.qualitative.Dark2)
fig.update_layout(title="Top 15 Countries with Deaths ", xaxis_title="Deaths", yaxis_title="Country", 
                      yaxis_categoryorder = 'total ascending',
                      uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()


# <span style=color:Green> - USA and Brazil are still our top 2 with the highest Deaths with nearly 5% probability wich means 5 of every 100 Confirmed cases may die in both countries.
#     
# <span style=color:Green> - Russia (landed third in Confirmed cases plot) has low number of deaths relative to the number of Confirmed cases with probability 1.3% .
#     
# <span style=color:Green>- There are 8 <b>European Countries</b> out of 15 country.

# ## Let's Visualize both cases with respect to continents....
# 
#     

# <h2><span style=color:blue> Idiom : <br>
#     
# <span style=color:red>Horizontal Stacked Bar Chart</span></span></h2>
#     
# <h2><span style=color:blue> Data </span></h2>
#     
# 
# -Categorical: <span style=color:red> Countries
#     
# -Categorical: <span style=color:red> Who Region
#     
# -Quantitative: <span style=color:red> Number Of Confirmed
#     
# <h2><span style=color:blue> Task </span></h2>
#     
# 
# <span style=color:red> Part to whole Comparisons between countries in the same continent with respect to their Confirmed cases.

# In[20]:


fig = px.bar(country_wise.sort_values("Confirmed").tail(10), x="Confirmed", y="WHO Region",
             color="Country/Region", barmode = 'stack')

fig.update_layout(title="Top 15 Countries with Confirmed cases", xaxis_title="Confirmed", yaxis_title="Continents", 
                      yaxis_categoryorder = 'total ascending',
                      uniformtext_minsize=8, uniformtext_mode='hide')
 
fig.show()


# <h2><span style=color:blue> Idiom : <br>
#     
# <span style=color:red>Horizontal Stacked Bar Chart</span></span></h2>
#     
# <h2><span style=color:blue> Data </span></h2>
#     
# 
# -Categorical: <span style=color:red> Countries
#     
# -Categorical: <span style=color:red> Who Region
#     
# -Quantitative: <span style=color:red> Number Of Deaths
#     
# <h2><span style=color:blue> Task </span></h2>
#     
# 
# <span style=color:red> Part to whole Comparisons between countries in the same continent with respect to their Deaths number.

# In[21]:


fig = px.bar(country_wise.sort_values("Deaths").tail(10), x="Deaths", y="WHO Region",
             color="Country/Region", barmode = 'stack')

fig.update_layout(title="Top 15 Countries with Deaths", xaxis_title="Deaths", yaxis_title="Continents", 
                      yaxis_categoryorder = 'total ascending',
                      uniformtext_minsize=8, uniformtext_mode='hide')
 
fig.show()


# # <span style=color:red> Question 3
# 
# ## What are the positions of our Continents and Region With respect to the number of
#     
#    ## Confirmed Cases?
# 
#     

# <h2><span style=color:blue> Idiom : <br>
#     
# <span style=color:red>Pie Chart</span></span></h2>
#     
# <h2><span style=color:blue> Data </span></h2>
#     
# 
#     
# -Categorical: <span style=color:red> Who Region
#     
# -Quantitative: <span style=color:red> Number Of Confirmed Cases
#     
# <h2><span style=color:blue> Task </span></h2>
#     
# 
# <span style=color:red> Part to whole Comparisons between continents with respect to their Confirmed Cases number.

# In[22]:


colors = ['blue', 'green', 'black', 'purple', 'red', 'brown']
fig = go.Figure(data=[go.Pie(labels=country_wise["WHO Region"], 
                       values=country_wise["Confirmed"])])
# Define hover info, text size, pull amount for each pie slice, and stroke
fig.update_traces(hoverinfo='label+percent', textfont_size=15,
                  textinfo='label+percent', pull=[0.1, 0, 0.2, 0, 0, 0],
                  marker=dict(colors=colors, line=dict(color='#FFFFFF', width=2)))
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))


# <b> The Continents positions according to the number of Confirmed Cases came : 
#     
# <span style=color:Green>    1-The Americas have the highest number of Confirmed Cases (Nearly half of our plot).
#     
# <span style=color:Green>     2-Europe
#     
# <span style=color:Green> <span style=color:Green> <span style=color:Green> <span style=color:Green>     3-Eastern Mediterranean
#     
# <span style=color:Green> <span style=color:Green> <span style=color:Green>     4-South-East Asia
#     
# <span style=color:Green> <span style=color:Green>     5-Western Pacific
#     
# <span style=color:Green>     6-Africa (The Least)
#     
# 

# # • So, We Compared the total number of deaths and recovered cases in 
# 
# # previous plots but that doesn't represent probability of death Or Survival 
# 
# # thus, we will use the derived attributes ("Deaths/100 Cases") 

# # <span style=color:red> Question 4
# 
# ## Who are the highest countries in probability of death due to infection?
# 
#     

# <h2><span style=color:blue> Idiom : <br>
#     
# <span style=color:red>Choropleth Map</span></span></h2>
#     
# <h2><span style=color:blue> Data </span></h2>
#     
# 
#     
# -Geographic Geometry:<span style=color:red> Locations Of Countries 
#     
# -1 Quantitative: <span style=color:red> Deaths / 100 Cases
#     
# <h2><span style=color:blue> Task </span></h2>
#     
# 
# <span style=color:red> Visualizing and understanding spatial relationships.

# In[23]:


df = country_wise[country_wise["Deaths/100 Cases"]>0]
fig = px.choropleth(df, locations="Country/Region", locationmode='country names', 
                  color='Deaths/100 Cases', hover_name="Country/Region", 
                  title='Deaths / 100 Cases', hover_data=['Deaths/100 Cases'], color_continuous_scale="matter")
fig.show()


# # To be Ordered

# In[24]:



fig = px.bar(country_wise.sort_values("Deaths/100 Cases").tail(20), 
                 x="Deaths/100 Cases", y="Country/Region", color='WHO Region',  
                 text="Deaths/100 Cases", orientation='h', width=700, 
                 color_discrete_sequence = px.colors.qualitative.Dark2)
fig.update_layout(title="Top 20 Countries with Deaths probabilities ", xaxis_title="Deaths/100 Cases", yaxis_title="Country", 
                      yaxis_categoryorder = 'total ascending',
                      uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()
    
 


# <span style=color:Green>-Yemen is leading our plot with the highest probability of Death.
#     
# <span style=color:Green>-There are 13 European Countries out of 20 Countries.
#    
# 

# # <span style=color:red> Question 5
# 
# ## Is there a relation between "Health Life Expectancy" and "Deaths/100 Cases" relative to countries?
# 
#     

# In[25]:


happiness_report = World_happ[['Country or region', 'Healthy life expectancy']]


# In[26]:


temp = country_wise.merge(happiness_report, left_on='Country/Region', right_on='Country or region')


# <h2><span style=color:blue> Idiom : <br>
#     
# <span style=color:red>Scatter Plot</span></span></h2>
#     
# <h2><span style=color:blue> Data </span></h2>
#     
# 
#     
# -Quantitative: <span style=color:red> Deaths/100 Cases
#     
# -Quantitative: <span style=color:red> Health Life Expectancy
#     
# <h2><span style=color:blue> Task </span></h2>
#     
# 
# <span style=color:red> Find realtionship between two quantitative values.(Can also detect trends, outliers, distribution, correlation and clusters) 

# In[27]:


px.scatter(temp, y='Deaths/100 Cases', x='Healthy life expectancy', color='WHO Region', hover_data=['Country/Region'],log_y=True)


# <span style=color:Green>There is no any noticed correlation between both attributes
#     
# 
#    
# 

# In[28]:


fig = px.scatter(country_wise, x='Confirmed', y='Recovered', color='WHO Region', 
                 height=700, hover_name='Country/Region', log_x=True, log_y=True
                 , 
                 title='Confirmed vs Recovered',
                 color_discrete_sequence=px.colors.qualitative.Vivid)
fig.update_traces(textposition='top center')
fig.show()


#  <span style=color:Green>-Overall there was a strong Positive Correletion between number of cases and Recovered Cases, Indicating that by the end of the year people were recovering.
#     
#  <span style=color:Green> -We nearly have 3 Outliers which are : (Haiti,Uk and Netherlands) having less surviving  people compared to other countries on the same levels.
#     
# 
#    
# 

#  

# # Calculating the Complexity of the whole Python Script <span style=color:red> Time and Memory Usage

# In[29]:


end = time.time()
time_taken=end-start
print(end - start)


# In[30]:


get_ipython().run_line_magic('memit', '')

