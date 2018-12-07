from interactions import *

#Begin feature engineering by removing features that have a low variance and high correlation

thresholder = VarianceThreshold(threshold=.5)

#function to filter out features with low variance
def variance_threshold_selector(data, threshold = .5):
    selector = VarianceThreshold(threshold)
    selector.fit(data)
    return data[data.columns[selector.get_support(indices=True)]]

#Dropping features that have a low variance

features_selected_train = variance_threshold_selector(features_interactions_train)

#Creating a correlation matrix
corr_matrix = features_selected_train.corr().abs()

upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape),k=1).astype(np.bool))

#Creating a list of columns to drop
to_drop = [column for column in upper.columns if any(upper[column]>0.95)]

#Drop certain highly correlated features
features_selected_train.drop(columns=to_drop,inplace=True)
features_selected_test = features_interactions_test[features_selected_train.columns]
