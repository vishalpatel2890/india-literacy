# india-literacy


Hello,

The purpose of our project was to determine what factors most influence the total literacy rate in India. 
We obtained data from a Kaggle dataset that gave us copious amounts of data on each district in India. Next, 
we spent some time studying the data and selected the most relevant features that we thought would impact the 
literacy rate. We then peformed exploratory data analysis and created a pandas Dataframe of useful features.

After EDA we started to perform linear regression testing on our data. We started of with a basic linear regression
in order to establish a baseline for our peformance. In addition, we calculated cross validation scores and RMSE
throughout our entire regression testing process. After establishing a baseline using basic linear regression, we 
began to perform feature engineering and feature selection. We removed features that have low variance and we also 
removed certain features that were highly correlated to each other. After inital feature selection we then re-ran 
our regression testing and recorded our results. Next, we used the SelectKBest class from sklearn to select the K
highest performing features. The scoring function we used to pick the features was the mutual_info_regression scoring
function. We then re-ran our regression test metrics. Following this testing, we then decided to implement a random forest
regressor on our dataset. Finally, we also optimized our regression using the Ridge Regression technique.

The three most relevant features affecting total literacy rate in in various Indian districts that we found were Male to Female Ratio,
the percentage of Owned Households, and the Total Purchasing Power of a household.

We really enjoyed completing this project and learning about the various different factors that affect literacy.

Please reach out if you have any questions about what we did.

Thank you,

Darshan Padmanabhan and Vishal Patel
