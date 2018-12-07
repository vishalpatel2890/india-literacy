from data import *
from sklearn import preprocessing
from sklearn import pipeline


#Initialize scaler
scaler = preprocessing.StandardScaler()

#Scale the numerical variables in our dataframe and create our training data set for features

#fit data to scaler (generate mean and std)
scaler.fit(X_train.iloc[:,:-3])
#transform data (apply z = (x-mean)/std)
features_scaled_train = pd.DataFrame(scaler.transform(X_train.iloc[:,:-3]), columns = X_train.columns[:-3], index = X_train.index)
#dataframe of just categorical variables
cat_variables = X_train.iloc[:, -3:]
features_scaled_train = pd.concat([features_scaled_train, cat_variables], axis=1)

#Scale the numerical variables in our dataframe and create our testing data set for features

scaler.fit(X_test.iloc[:,:-3])
features_scaled_test = pd.DataFrame(scaler.transform(X_test.iloc[:,:-3]), columns = X_test.columns[:-3], index = X_test.index)
cat_variables_test = X_test.iloc[:, -3:]
features_scaled_test = pd.concat([features_scaled_test, cat_variables_test], axis=1)

#Renaming the columns of our categorical variables

features_scaled_train.rename(columns={features_scaled_train.columns[5]: 'HINDUS ZERO TO 33%',
                                    features_scaled_train.columns[6]: 'HINDUS 66% TO 100%',
                                    features_scaled_train.columns[7]:'OWNERSHIP OF HOUSEHOLDS > MEAN'
                               }, inplace=True)

features_scaled_test.rename(columns={features_scaled_test.columns[5]: 'HINDUS ZERO TO 33%',
                                    features_scaled_test.columns[6]: 'HINDUS 66% TO 100%',
                                    features_scaled_test.columns[7]:'OWNERSHIP OF HOUSEHOLDS > MEAN'
                               }, inplace=True)
