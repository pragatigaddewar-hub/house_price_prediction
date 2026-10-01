import pandas as pd

## Data Collection
df = pd.read_csv('House Price Prediction Dataset.csv')

## Data Understanding
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.columns)
df.info()
print(df.describe())

## Data Cleaning
# 1. Check Missing Values
print("Missing Values :" ,df.isnull().sum())

# 2. Check Duplicate Values
print("Duplicate Values :" ,df.duplicated().sum())

# 3. Outliers
# Numerical Columns
num_cols = df.select_dtypes(include='number').columns
print("Numerical Columns :" ,num_cols)

# Area Column
Q1 = df['Area'].quantile(0.25)
Q3 = df['Area'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR 
upper_limit = Q3 + 1.5 * IQR 

outliers = (df['Area'] < lower_limit)  | (df['Area'] > upper_limit)
print("Outliers of Area :" ,outliers.sum())


# Bedrooms Column
Q1 = df['Bedrooms'].quantile(0.25)
Q3 = df['Bedrooms'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR 
upper_limit = Q3 + 1.5 * IQR 

outliers = (df['Bedrooms'] < lower_limit)  | (df['Bedrooms'] > upper_limit)
print("Outliers of Bedrooms:" ,outliers.sum())


# Bathrooms Column
Q1 = df['Bathrooms'].quantile(0.25)
Q3 = df['Bathrooms'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR 
upper_limit = Q3 + 1.5 * IQR 

outliers = (df['Bathrooms'] < lower_limit)  | (df['Bathrooms'] > upper_limit)
print("Outliers of Bathrooms:" ,outliers.sum())


# Floors Column
Q1 = df['Floors'].quantile(0.25)
Q3 = df['Floors'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR 
upper_limit = Q3 + 1.5 * IQR 

outliers = (df['Floors'] < lower_limit)  | (df['Floors'] > upper_limit)
print("Outliers of Floors:" ,outliers.sum())


# YearBuilt Column
Q1 = df['YearBuilt'].quantile(0.25)
Q3 = df['YearBuilt'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR 
upper_limit = Q3 + 1.5 * IQR 

outliers = (df['YearBuilt'] < lower_limit)  | (df['YearBuilt'] > upper_limit)
print("Outliers of YearBuilt:" ,outliers.sum())


# 4. Check Invalid/Incorrect Values
# Numerical Columns

print("Area_Min :" ,df['Area'].min())
print("Area_Max :" ,df['Area'].max())

print("Bedrooms_Min :" ,df['Bedrooms'].min())
print("Bedrooms_Max :" ,df['Bedrooms'].max())

print("Bathrooms_Min :" ,df['Bathrooms'].min())
print("Bathrooms_Max :" ,df['Bathrooms'].max())

print("Floors_Min :" ,df['Floors'].min())
print("Floors_Max :" ,df['Floors'].max())

print("YearBuilt_Min :" ,df['YearBuilt'].min())
print("YearBuilt_Max :" ,df['YearBuilt'].max())

print("Price_Min :" ,df['Price'].min())
print("Price_Max :" ,df['Price'].max())

# Categorical Columns
categ_cols = df.select_dtypes(include='object').columns
print("Categorical Columns :" ,categ_cols)

print("Value Counts of Location :" ,df['Location'].value_counts())
print("Value Counts of Condition :" ,df['Condition'].value_counts())
print("Value Counts of Garage :" ,df['Garage'].value_counts())

## EDA
# Univariate Analysis
# Distribution Of Numerical Columns 
import matplotlib.pyplot as plt

plt.hist(df['Area'])
plt.xlabel("Area")
plt.ylabel("Count")
plt.title("Distribution Of Area")
plt.show()


plt.hist(df['Bedrooms'])
plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.title("Distribution Of Bedrooms")
plt.show()


plt.hist(df['Bathrooms'])
plt.xlabel("Bathrooms")
plt.ylabel("Count")
plt.title("Distribution Of Bathrooms")
plt.show()


plt.hist(df['Floors'])
plt.xlabel("Floors")
plt.ylabel("Count")
plt.title("Distribution Of Floors")
plt.show()


plt.hist(df['YearBuilt'])
plt.xlabel("YearBuilt")
plt.ylabel("Count")
plt.title("Distribution Of YearBuilt")
plt.show()


plt.hist(df['Price'])
plt.xlabel("Price")
plt.ylabel("Count")
plt.title("Distribution Of Price")
plt.show()

# Distribution Of Categorical Columns
plt.bar(df['Location'].value_counts().index , df['Location'].value_counts().values)
plt.xlabel("Location")
plt.ylabel("Count")
plt.title("Distribution Of Location")
plt.show()

plt.bar(df['Condition'].value_counts().index , df['Condition'].value_counts().values)
plt.xlabel("Condition")
plt.ylabel("Count")
plt.title("Distribution Of Condition")
plt.show()

plt.bar(df['Garage'].value_counts().index , df['Garage'].value_counts().values)
plt.xlabel("Garage")
plt.ylabel("Count")
plt.title("Distribution Of Garage")
plt.show()


# Bivariate Analysis

import seaborn as sns

# Numerical Columns
sns.scatterplot(data=df,x='Area',y='Price')
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area VS Price")
plt.show()


sns.scatterplot(data=df,x='Bedrooms',y='Price')
plt.xlabel("Bedrooms")
plt.ylabel("Price")
plt.title("Bedrooms VS Price")
plt.show()


sns.scatterplot(data=df,x='Bathrooms',y='Price')
plt.xlabel("Bathrooms")
plt.ylabel("Price")
plt.title("Bathrooms VS Price")
plt.show()


sns.scatterplot(data=df,x='Floors',y='Price')
plt.xlabel("Floors")
plt.ylabel("Price")
plt.title("Floors VS Price")
plt.show()


sns.scatterplot(data=df,x='YearBuilt',y='Price')
plt.xlabel("YearBuilt")
plt.ylabel("Price")
plt.title("YearBuilt VS Price")
plt.show()


# Categorical Columns
sns.barplot(data=df,x='Location',y='Price')
plt.xlabel("Location")
plt.ylabel("Price")
plt.title("Location VS Price")
plt.show()


sns.barplot(data=df,x='Condition',y='Price')
plt.xlabel("Condition")
plt.ylabel("Price")
plt.title("Condition VS Price")
plt.show()


sns.barplot(data=df,x='Garage',y='Price')
plt.xlabel("Garage")
plt.ylabel("Price")
plt.title("Garage VS Price")
plt.show()

# Multivariate Analysis
# Correlation
print("Correlation :" ,df[num_cols].corr())

# Heatmap
sns.heatmap(df[num_cols].corr(),annot=True)


## Feature Selection
df = df.drop('Id',axis =1)
print(df.columns)

## Data processing
# 1. Encoding
# One-Hot Encoding
one_hot = pd.get_dummies(df[['Location','Condition']])
print(one_hot)

# Ordinal Encoding
from sklearn.preprocessing import OrdinalEncoder
ordinal = OrdinalEncoder()
garage_encoded = ordinal.fit_transform(df[['Garage']])
garage_encoded_df = pd.DataFrame(garage_encoded , columns=['Garage'])

final_encoding_df = pd.concat([one_hot,garage_encoded_df],axis=1)

new_nums_cols = df.select_dtypes(include='number').columns.drop('Price')
print(new_nums_cols)

X = pd.concat([df[new_nums_cols],final_encoding_df],axis=1)
y = df["Price"]

# 2. Train-Test Split
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42,test_size=0.2)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

# 3. Feature Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)

X_test_scaled = scaler.transform(X_test)

## Model Bulding
# Model 1 : Linear Regression
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train_scaled,y_train)
y_pred = model.predict(X_test_scaled)

## Evaluation
from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error,r2_score
print("Linear Regression")
# MAE
lr_mae = mean_absolute_error(y_test,y_pred)
print("MAE :" ,lr_mae)

# MSE
lr_mse = mean_squared_error(y_test,y_pred)
print("MSE :" ,lr_mse)

# RMSE
lr_rmse = root_mean_squared_error(y_test,y_pred)
print("RMSE :" ,lr_rmse)

# R2 Score
lr_r2 = r2_score(y_test,y_pred)
print("R2 Score :" ,lr_r2)

# Model 2 : Multiple Linear Regression
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train_scaled,y_train)
y_pred = model.predict(X_test_scaled)

## Evaluation
print("Multiple Regression")
# MAE
multiple_mae = mean_absolute_error(y_test,y_pred)
print("MAE :" ,multiple_mae)

# MSE
multiple_mse = mean_squared_error(y_test,y_pred)
print("MSE :" ,multiple_mse)

# RMSE
multiple_rmse = root_mean_squared_error(y_test,y_pred)
print("RMSE :" ,multiple_rmse)

# R2 Score
multiple_r2 = r2_score(y_test,y_pred)
print("R2 Score :" ,multiple_r2)

# Model 3 : Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

model = LinearRegression()
model.fit(X_train_poly,y_train)
y_pred = model.predict(X_test_poly)

## Evaluation
print("Polynomial Regression")
# MAE
poly_mae = mean_absolute_error(y_test,y_pred)
print("MAE :" ,poly_mae)

# MSE
poly_mse = mean_squared_error(y_test,y_pred)
print("MSE :" ,poly_mse)

# RMSE
poly_rmse = root_mean_squared_error(y_test,y_pred)
print("RMSE :" ,poly_rmse)

# R2 Score
poly_r2 = r2_score(y_test,y_pred)
print("R2 Score :" ,poly_r2)

# Model 4. Decision Tree Regression
from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

## Evaluation
print("Decision Tree Regression")
# MAE
dt_mae = mean_absolute_error(y_test,y_pred)
print("MAE :" ,dt_mae)

# MSE
dt_mse = mean_squared_error(y_test,y_pred)
print("MSE :" ,dt_mse)

# RMSE
dt_rmse = root_mean_squared_error(y_test,y_pred)
print("RMSE :" ,dt_rmse)

# R2 Score
dt_r2 = r2_score(y_test,y_pred)
print("R2 Score :" ,dt_r2)

# Model 5. Random Forest Regression
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

## Evaluation
print("Random Forest Regression")
# MAE
rf_mae = mean_absolute_error(y_test,y_pred)
print("MAE :" ,rf_mae)

# MSE
rf_mse = mean_squared_error(y_test,y_pred)
print("MSE :" ,rf_mse)

# RMSE
rf_rmse = root_mean_squared_error(y_test,y_pred)
print("RMSE :" ,rf_rmse)

# R2 Score
rf_r2 = r2_score(y_test,y_pred)
print("R2 Score :" ,rf_r2)


## Model Comparison

comparison = pd.DataFrame({
    'Model' : [
        'Linear Regression' ,
        'Multiple Regression' ,
        'Polynomial Regression' ,
        'Decision Tree Regression',
        'Random Forest Regression'
    ] ,
    'MAE' : [
        lr_mae,
        multiple_mae,
        poly_mae,
        dt_mae,
        rf_mae
    ] ,
    'MSE' : [
        lr_mse,
        multiple_mse,
        poly_mse,
        dt_mse,
        rf_mse 
    ],
    'RMSE' : [
        lr_rmse,
        multiple_rmse,
        poly_rmse,
        dt_rmse,
        rf_rmse
    ],
    'R2 Score' : [
        lr_r2,
        multiple_r2,
        poly_r2,
        dt_r2,
        rf_r2
    ]
})

print("Comparison :" ,comparison)

## Target Leakage
print('Price' in X)

## Final Model Selection
final_model = LinearRegression()
final_model.fit(X,y)
print("Final Model : Linear Regression")

## New / Unseen Data 
print(X.columns)

new_data = pd.DataFrame({
    'Area': [2000],
    'Bedrooms': [3],
    'Bathrooms': [2],
    'Floors': [2],
    'YearBuilt': [2015],
    'Location_Downtown': [0],
    'Location_Rural': [0],
    'Location_Suburban': [0],
    'Location_Urban': [1],
    'Condition_Excellent': [0],
    'Condition_Fair': [0],
    'Condition_Good': [1],
    'Condition_Poor': [0],
    'Garage': [1]
})

## Final Model prediction
prediction = final_model.predict(new_data[X.columns])
print("Prediction :" ,prediction)