import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#read census data into pandas dataframe selecting only relevant columns
census_2011 = pd.read_csv('./2011-india-census/india-districts-census-2011.csv',
                            usecols=list(range(1,9)) + list(range(25,26)) +  list(range(35,40)) + list(range(68,70)) + list(range(117,118)))
'''
Create new columns representing potentially useful features for regression algorithm
New Columns:
Percentage of Owned Households per district
Male to Female Ratio per district
Total Literacy Rate per district
Percentage of Urban Households per district
Percentage of Households with Internet per district
Percentage of Hindus per district

'''

census_2011['Percentage of Owned Households'] = census_2011['Ownership_Owned_Households']/census_2011['Households']
census_2011['Male to Female Ratio'] = census_2011['Male']/census_2011['Female']
census_2011['Total Literacy Rate'] = census_2011['Literate']/census_2011['Population']
census_2011['Percentage of Urban Households'] = census_2011['Urban_Households']/census_2011['Households']
census_2011['Percentage of Households with Internet'] = census_2011['Households_with_Internet']/census_2011['Households']
census_2011['Percentage Hindu'] = census_2011['Hindus']/census_2011['Population']

#Create a categorical variable representing the percentage of hindus in each district in India
bins = [0, .33, .66, 1]
census_2011['Binned Hindu'] = pd.cut(census_2011['Percentage Hindu'], bins)
hindus = pd.get_dummies(census_2011['Binned Hindu'], drop_first=True)
census_2011 = pd.concat([census_2011, hindus], axis=1)

#Create a categorical variable representing the percentage of owned households in each district in India
av = np.average(census_2011['Percentage of Owned Households'], weights = census_2011['Population'])
bins_av = [0,av,1]
census_2011['Binned Ownership'] = pd.cut(census_2011['Percentage of Owned Households'], bins_av)
ownership = pd.get_dummies(census_2011['Binned Ownership'],drop_first=True)
census_2011 = pd.concat([census_2011,ownership], axis = 1)

#Drop categorical variable columns
census_2011=census_2011.drop(columns=['Binned Ownership', 'Binned Hindu', 'Percentage Hindu'])

#select only relevant columns
data = census_2011.iloc[:, -10:]

# separate y target
target = census_2011['Total Literacy Rate']

# drop target leaving only features to build model on
features = data.drop(columns=['Total Literacy Rate'])

#split training and test data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
