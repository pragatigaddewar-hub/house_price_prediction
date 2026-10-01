# House Price Prediction

## Project Overview

This project uses Machine Learning regression algorithms to predict house prices based on features such as area, bedrooms, bathrooms, floors, year built, location, condition, and garage availability.

## Dataset

* Dataset: House Price Prediction Dataset
* Rows: 2000
* Features: 9 input features after removing `Id`
* Target: `Price`

### Features

* Area
* Bedrooms
* Bathrooms
* Floors
* YearBuilt
* Location
* Condition
* Garage

## Data Preprocessing

The following steps were performed:

* Checked missing values
* Checked duplicate values
* Checked numerical outliers using IQR
* Checked invalid/incorrect values
* Analyzed categorical feature distributions
* Removed `Id` from the dataset
* Applied One-Hot Encoding to `Location` and `Condition`
* Applied Ordinal Encoding to `Garage`
* Split the data into training and testing sets
* Applied feature scaling for Linear and Polynomial Regression models

## Exploratory Data Analysis

Performed:

* Univariate analysis
* Bivariate analysis
* Multivariate analysis
* Distribution plots
* Scatter plots
* Categorical feature analysis
* Correlation analysis
* Correlation heatmap

## Machine Learning Models

The following regression models were implemented:

1. Linear Regression
2. Multiple Linear Regression
3. Polynomial Regression
4. Decision Tree Regression
5. Random Forest Regression

## Model Evaluation

Models were evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

A model comparison was performed using these evaluation metrics.

## Final Model

Linear Regression was selected as the final model based on the comparative evaluation results.

The final model was trained on the complete feature set (`X, y`) and used to predict the price of new/unseen house data.

## New / Unseen Data Prediction

The final model was tested on a new house input with previously unseen feature values.

Example:

* Area: 2000
* Bedrooms: 3
* Bathrooms: 2
* Floors: 2
* Year Built: 2015
* Location: Urban
* Condition: Good
* Garage: Yes

Predicted Price:

**₹515,480.93**

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook / VS Code

## Project Structure

```text
house-price-prediction/
│
├── house_price_prediction.py
├── House Price Prediction Dataset.csv
└── README.md
```
