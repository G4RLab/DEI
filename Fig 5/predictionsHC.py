#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd

# Load the data
data_path = 'High Confidence Data - Sheet2.csv'
data = pd.read_csv(data_path)

# Display the first few rows of the dataframe to understand its structure
data.head()


# In[9]:


# Group data by "Publication Year" and "Gender" and count the number of occurrences
author_counts_by_year_gender = data.groupby(['Publication Year', 'Gender']).size().unstack(fill_value=0)

# Display the aggregated data
author_counts_by_year_gender


# In[10]:


from numpy import polyfit, polyval
from sklearn.metrics import mean_squared_error

# Filter data for pre-pandemic years for modeling
pre_pandemic_data = author_counts_by_year_gender[author_counts_by_year_gender.index <= 2019]

# Prepare data for modeling
years = pre_pandemic_data.index.values
male_authors = pre_pandemic_data['male'].values
female_authors = pre_pandemic_data['female'].values

# Polynomial degree (let's start with a quadratic model, degree=2)
degree = 2

# Fit the models
male_model = polyfit(years, male_authors, degree)
female_model = polyfit(years, female_authors, degree)

# Years for forecasting
forecast_years = [2020, 2021, 2022, 2023]

# Forecasting
male_forecasts = polyval(male_model, forecast_years)
female_forecasts = polyval(female_model, forecast_years)

# Actual data for comparison
actual_male = author_counts_by_year_gender.loc[forecast_years, 'male'].values
actual_female = author_counts_by_year_gender.loc[forecast_years, 'female'].values

# Prepare a DataFrame for manuscript-ready table
forecast_vs_actual = pd.DataFrame({
    'Year': forecast_years,
    'Forecasted Male Authors': male_forecasts.round(0),
    'Actual Male Authors': actual_male,
    'Forecasted Female Authors': female_forecasts.round(0),
    'Actual Female Authors': actual_female
})
print(male_authors)
forecast_vs_actual


# In[12]:


# Calculate Mean Squared Error (MSE) for each forecast against actual data

# MSE for male authors
mse_male = mean_squared_error(actual_male, male_forecasts)

# MSE for female authors
mse_female = mean_squared_error(actual_female, female_forecasts)

mse_male, mse_female


# In[13]:


# Function to print the polynomial equation from coefficients
def print_polynomial_equation(coefficients, label="Model"):
    # Assuming a quadratic model, coefficients are in the order of [c, b, a]
    a, b, c = coefficients
    print(f"{label} Authors Model: y = {a:.4f}x^2 + {b:.4f}x + {c:.4f}")

# Print the equations for both models
print_polynomial_equation(male_model, "Male")
print_polynomial_equation(female_model, "Female")


# In[14]:


from sklearn.metrics import mean_squared_error, r2_score

# Calculate RMSE and R-squared for males
rmse_male = np.sqrt(mean_squared_error(male_authors, polyval(male_model, years)))
r_squared_male = r2_score(male_authors, polyval(male_model, years))

# Calculate RMSE and R-squared for females
rmse_female = np.sqrt(mean_squared_error(female_authors, polyval(female_model, years)))
r_squared_female = r2_score(female_authors, polyval(female_model, years))

print(f"Male - RMSE: {rmse_male:.2f}, R-squared: {r_squared_male:.2f}")
print(f"Female - RMSE: {rmse_female:.2f}, R-squared: {r_squared_female:.2f}")


# In[15]:


import numpy as np

# Splitting the data into pre- and post-2020
pre_2020_data = author_counts_by_year_gender[author_counts_by_year_gender.index < 2020]
post_2020_data = author_counts_by_year_gender[author_counts_by_year_gender.index >= 2020]

# Fitting separate models for pre- and post-2020 data
# Pre-2020
pre_years = pre_2020_data.index.values
pre_male_authors = pre_2020_data['male'].values
pre_female_authors = pre_2020_data['female'].values
pre_male_model = polyfit(pre_years, pre_male_authors, degree)
pre_female_model = polyfit(pre_years, pre_female_authors, degree)

# Post-2020
post_years = post_2020_data.index.values
post_male_authors = post_2020_data['male'].values
post_female_authors = post_2020_data['female'].values
post_male_model = polyfit(post_years, post_male_authors, degree)
post_female_model = polyfit(post_years, post_female_authors, degree)

# Predicting values at 2020 to assess discontinuity
pre_2020_male_predict = polyval(pre_male_model, 2020)
post_2020_male_predict = polyval(post_male_model, 2020)
male_discontinuity = post_2020_male_predict - pre_2020_male_predict

pre_2020_female_predict = polyval(pre_female_model, 2020)
post_2020_female_predict = polyval(post_female_model, 2020)
female_discontinuity = post_2020_female_predict - pre_2020_female_predict

(pre_2020_male_predict, post_2020_male_predict, male_discontinuity, pre_2020_female_predict, post_2020_female_predict, female_discontinuity)


# In[16]:


# Preparing the full range of years in the dataset
full_years = author_counts_by_year_gender.index.values

# Splitting the full range into pre- and post-2020
pre_years_full = full_years[full_years < 2020]
post_years_full = full_years[full_years >= 2020]

# Predicting counts for all years using the respective models
# Male authors
pre_male_predictions = polyval(pre_male_model, pre_years_full)
post_male_predictions = polyval(post_male_model, post_years_full)
full_male_predictions = np.concatenate([pre_male_predictions, post_male_predictions])

# Female authors
pre_female_predictions = polyval(pre_female_model, pre_years_full)
post_female_predictions = polyval(post_female_model, post_years_full)
full_female_predictions = np.concatenate([pre_female_predictions, post_female_predictions])

# Compiling results
predictions_df = pd.DataFrame({
    'Year': full_years,
    'Predicted Male Authors': full_male_predictions.round(0),
    'Predicted Female Authors': full_female_predictions.round(0)
})

predictions_df


# In[ ]:




