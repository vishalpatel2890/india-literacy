from scaling import *
from sklearn.feature_selection import RFE, VarianceThreshold

#Using Polynomial Features to transform our dataframe and get more features

poly = preprocessing.PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
features_interactions_train = pd.DataFrame(poly.fit_transform(features_scaled_train), columns=poly.get_feature_names(features_scaled_train.columns))
features_interactions_test = pd.DataFrame(poly.fit_transform(features_scaled_test), columns=poly.get_feature_names(features_scaled_test.columns))
