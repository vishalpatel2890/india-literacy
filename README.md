# Using Linear Regression to Predict Literacy Rates in Districts in India


## Goal
Create a model that accurately predicts literacy rates in districts in India.

## EDA
We obtained India's 2011 census data from [Kaggle](https://www.kaggle.com/danofer/india-census#india-districts-census-2011.csv "Kaggle Dataset") that gave us copious amounts of data on each district in India. Next, 
we spent some time studying the data and selected the most relevant features that we thought would impact the 
literacy rate. We ultimately decided to look at the following features :
* Total Purchase Power Parity
* Percentage Owner Occupied Households
* Male to Female Ratio
* Percentage of Urban Households
* Percentage of Households with Internet
* Tercile of Percentage of the Population that is Hindu

## Baseline
After EDA we performed linear regression testing on our full feature set. We started of with a basic linear regression
in order to establish a baseline for our peformance. In addition, we calculated cross validation scores and RMSE
throughout our entire regression testing process. 

**Baseline Stats**: 

R2: 0.5404890604922513 

AdjustR2: 0.509597568760638

MSE: 0.005385920249207483

RMSE: 0.07338882918542497

Normalized RMSE: 0.6752192312818441

## Feature Engineering
After running our baseline model we decided to test for interactions between our features. After generating our interaction features we removed all the features that had too low of variance to be of significant importance. Next we examined our interaction features for high correlation. 

![alt text](https://github.com/vishalpatel2890/india-literacy/blob/master/corr-heatmap.png "Correlation Heatmap")


The points in red show high correlation between two of our features and we subsequently removed them from our dataset. After inital feature selection we then re-ran our regression testing and recorded our results. 

Next, we used the SelectKBest class from sklearn to select the K highest performing features. The scoring function we used to pick the features was the mutual_info_regression scoring function. 
Following this testing, we then decided to implement a random forest regressor on our dataset. 

Finally, we also performed Ridge Regression technique on our entire feature set. The Ridge Regression proved to be the most accurate model (lowest RMSE) for our feature set: 

R2 0.48896269666875436

Adjusted R2: 0.47730076375149555

MSE: 0.004389889618438487

RMSE: 0.06625624210924196

Normalized RMSE: 0.6095953479730806

The most relevant features affecting total literacy rate in in various Indian districts that we found were:
* Male to Female Ratio interaction with HINDUS ZERO TO 33% (Negatively Correlated) 
* Percentage of Households with Internet interaction with OWNERSHIP OF HOUSEHOLDS > MEAN (Positively Correlated) 

![alt text](https://github.com/vishalpatel2890/india-literacy/blob/master/ridge_coef_plot.png "Coefficient values of each feature")

Each feature passed through the ridge regression and its respective coefficient.

![alt text](https://github.com/vishalpatel2890/india-literacy/blob/master/ridge_residuals.png "Residual Errors Plot")

Graph of our model predicted values versus our actual values

While our model is not useable due to inaccuracy this was a very interesting dive into regression and we really enjoyed completing this project and learning about the various different factors that affect literacy.

Please reach out if you have any questions about what we did.


Darshan Padmanabhan and Vishal Patel
