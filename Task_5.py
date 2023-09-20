import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

df = pd.read_csv('Advertising.csv')

# Check information about missing values
df.isnull().values.any()

df.describe()


# Scatter plots to check the linearity assumption between each independent variable (TV, Radio, Newspaper) and the dependent variable (Sales)
sns.pairplot(df, x_vars=["TV", "Radio", "Newspaper"], y_vars="Sales", kind="reg")

# Histograms to check the normality assumption of the dependent variable (Sales)
df.hist(bins=20, figsize=(12, 9))

# Linear regression plots to visualize the relationship between each independent variable and the dependent variable
sns.lmplot(x='TV', y='Sales', data=df)
sns.lmplot(x='Radio', y='Sales', data=df)
sns.lmplot(x='Newspaper', y='Sales', data=df)


X = df.drop('Sales', axis=1)
y = df[["Sales"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

import statsmodels.formula.api as sm
lin_model = sm.ols(formula="Sales ~ TV + Radio + Newspaper", data=df).fit()

# Print the coefficients of the linear model
print(lin_model.params, "\n")


new_data = pd.DataFrame({'TV': [1000], 'Radio': [500], 'Newspaper': [250]})
predicted_sales = lin_model.predict(new_data)
print("Predicted Sales :", predicted_sales)

new_data = pd.DataFrame({'TV': [100], 'Radio': [50], 'Newspaper': [25]})
predicted_sales = lin_model.predict(new_data)
print("Predicted Sales :", predicted_sales)
