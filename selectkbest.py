from biasvariance import *
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_regression

#function to return feature with strongest effect on target (outcome)
def information_selector(X, y, scoring, k=5):
    selector = SelectKBest(score_func=scoring, k=k)
    selector.fit(X, y)
    return X[X.columns[selector.get_support(indices=True)]]

#initalize SelectKBest and fit it to our data
test = SelectKBest(score_func=mutual_info_regression, k=12)
fit = test.fit(features_selected_train, y_train)

#features with most effect
features_selected_train_k_best = information_selector(features_selected_train, y_train, mutual_info_regression, k=12)
