# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:23:12 2020

@author: Kal
"""

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats
import pandas as pd
import statsmodels.api as sm


filename = r"C:\Users\Kal\Documents\Countdown Projects\Countdown Project 2\Data\movieData.csv"
data = pd.read_csv(filename)
df = pd.DataFrame(data)
print(data.head())
# examine relationship between popularity (rank) and time to crack (offline_crack_sec)

def isAnimated(x):
    if "Animation" in x:
        return "Yes"
    else:
        return "No"

def genresMultiple(x):
    count = 1
    for a in x: 
        if a == ",":
            count+=1
    return count

def leadActor(x):
    if "," in x:
        actor = x[0:x.find(",")]
        return actor
    else:
        actor = x
        return actor
    
def ratingIntervals(x):
    if 8 <=x:
        return "Good (8+)"
    if 6.5 <=x and 8 > x:
        return "Decent (6.5-8)"
    if 6.5 >x:
        return "Bad (0-6.5)"

    
data['Animation?'] = data["Genre"].apply(isAnimated)
data['HowManyGenres'] = data["Genre"].apply(genresMultiple)
data['LeadActor'] = data["Actors"].apply(leadActor)
data['Score'] = data["Rating"].apply(ratingIntervals)
n = 5
topActors = data['LeadActor'].value_counts()[:n].index.tolist()

def topLeadActor(x):
    if x in topActors:
        lastName = x[x.find(" "):len(x)]
        return lastName
    
data["TopLeadActor?"] = data['LeadActor'].apply(topLeadActor)
#actionData = data["Action" in data["Genre"] == True]
print(data.head())

# Histograms (for continuous variables)
plt.hist(data["Rating"], edgecolor='black', color='purple') # edgecolor outlines the bars, color fills the bars
plt.title('Movie Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Number of Movies')
plt.show()

sns.relplot(x= "Rating", y= "Revenue", color = "blue", data=data, kind ="line", hue="Animation?", palette = ["darkblue","lightgreen"])
plt.title("Relationship between Rating and Revenue")
plt.show()

#Do animated movies produce more revenue?
sns.catplot(x = 'Animation?', y = 'Revenue', kind = 'violin',palette = ["darkblue","lightgreen"], 
            data = data)
plt.title("Animated Movies and Revenue")
plt.ylabel("Revenue (Millions)")
plt.show()

#Do Movies with Multiple Genre = more revenue
sns.catplot(x = 'HowManyGenres', y = 'Revenue', kind = 'boxen', 
plt.title("Does Multiple Genres = More Revenue?")
plt.show()

            data = data)
plt.xticks(rotation = 0)
sns.catplot(x = 'TopLeadActor?', kind = "count", data = data, color = "pink",edgecolor = "black")
plt.xlabel('Top Lead Actors')
plt.ylabel('Number of Movies with Lead Role')
plt.show()


sns.catplot(x = 'TopLeadActor?', y = 'Revenue', kind = 'boxen', hue = 'Score',
            palette = ['green', 'yellow', 'red'],data = data)
plt.xticks(rotation = 0)
plt.xlabel("Top Five Actors with the Most Lead Roles ")
plt.ylabel("Movie Revenue (Millions)")
plt.show()

sns.catplot(x = 'TopLeadActor?', y = 'Revenue', kind = 'swarm', hue = 'Score',
            palette = ['green', 'yellow', 'red'],data = data)
plt.xticks(rotation = 0)

plt.xlabel("Top Five Actors with the Most Lead Roles ")
plt.ylabel("Movie Revenue (Millions)")
plt.show()

#Who are the best directors?

topData = data[data['Rating'] >= 8].sort_values('Rating', ascending = False)
n = 5
directors = topData['Director'].value_counts()[:n].index.tolist()

def topDirectors(x):
    if x in directors:
        #lastName = x[x.find(" "):len(x)]
        return x

topData["Top Directors"] = topData["Director"].apply(topDirectors)
sns.catplot(x = 'Top Directors', y= "Rating", kind = 'boxen', data= topData, palette = ["purple","blue","green","orange","red"])
plt.xticks(rotation = 35)
plt.title("Directors with the Most High-rated Movies (8+)")
plt.ylabel("Movie Rating")

plt.show()
# combining the two plots above 
sns.relplot(x='Rating', y='Revenue', hue = 'Top Directors', legend = "brief",
            palette = ["purple","blue","green","orange", "red"],data = topData)
plt.title('Revenue and Rating for Top Movies')
plt.ylabel("Revenue (Millions)")

plt.show()
sns.catplot(x = 'Top Directors', kind = "count", data = topData, color = "maroon",edgecolor = "yellow")
plt.xlabel('Top Directors')
plt.xticks(rotation = 35)
plt.ylabel('Number of 8+ Movies Directed')
plt.show()

#Rating vs Metascore, which do we trust?
# plotting regression lines on scatterplots
sns.lmplot(x = 'Rating', y='Metascore', data = data)
plt.title('Median Salary vs Share of Women in a Particular Major')
plt.show()

sns.catplot(x = 'Animation?', y = 'Rating', kind = 'swarm',palette = ["darkblue","lightgreen"], 
            data = data)
plt.title("Animated Movies and Rating")
plt.ylabel("Rating")
plt.show()
"""
revenue = data["Revenue"]
revenue2014 = data.Revenue[data.Year == 2014]
years = data["Year"]
rating = data.Rating[data.Year == 2014]
X = rating
X = sm.add_constant(X)
y = revenue2014
model = sm.OLS(y, X).fit()
model_output = model.summary()
print(model_output)
"""