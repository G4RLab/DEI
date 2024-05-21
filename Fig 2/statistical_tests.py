#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from scipy.stats import kendalltau


years_ca = [1991, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 
            2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 
            2017, 2018, 2019, 2020, 2021, 2022, 2023]
male_counts_ca = [2, 1, 1, 2, 1, 8, 8, 21, 18, 21, 44, 76, 92, 131, 122, 166, 186, 253, 237, 289, 
                  281, 346, 373, 466, 421, 498, 444, 596, 690, 772, 650]
female_counts_ca = [0, 0, 1, 0, 0, 2, 3, 1, 7, 11, 11, 17, 28, 33, 58, 52, 76, 85, 107, 110, 
                    148, 166, 165, 206, 223, 263, 280, 316, 381, 412, 440]
gender_gap_ca = [f - m for m, f in zip(male_counts_ca, female_counts_ca)]

# FA Dataset
years_fa = [1991, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 
            2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 
            2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
male_counts_fa = [1, 2, 2, 2, 1, 6, 10, 9, 9, 25, 32, 43, 90, 104, 125, 161, 215, 216, 242, 
                  245, 301, 298, 322, 297, 326, 308, 402, 461, 483, 453]
female_counts_fa = [1, 0, 1, 2, 0, 4, 2, 2, 9, 7, 17, 25, 57, 74, 98, 99, 132, 134, 172, 188, 
                    210, 234, 281, 270, 339, 318, 369, 438, 436, 460]
gender_gap_fa = [m-f for m, f in zip(male_counts_fa, female_counts_fa)]

# Mann-Kendall Test
mk_test_result_ca = kendalltau(years_ca, gender_gap_ca)
mk_test_result_fa = kendalltau(years_fa, gender_gap_fa)

# Results
print("CA Dataset Mann-Kendall Test Result:", mk_test_result_ca)
print("FA Dataset Mann-Kendall Test Result:", mk_test_result_fa)


# In[3]:


from scipy.stats import chi2_contingency

# Observed frequencies
data = {
    "China": [1747, 839],
    "USA": [1663, 715],
    "Germany": [506, 203],
    "Japan": [442, 73],
    "England": [256, 124]
}

# Perform chi-squared test for each country
results = {}
for country, frequencies in data.items():
    chi2, p_value, _, _ = chi2_contingency([frequencies, [sum(frequencies) - f for f in frequencies]])
    results[country] = {'Chi-squared': chi2, 'p-value': p_value}

results
'''This test helps us determine if there is a significant difference between the number of males and females in each country'''


# In[1]:


import pandas as pd

# Load the Excel file
file_path = 'Publications_Forecast.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataframe to understand its structure
data.head()
# Load the Excel file and list the sheet names
sheets = pd.ExcelFile(file_path)
sheet_names = sheets.sheet_names

# Read and preview the first few rows of each sheet
sheets_data = {}
for sheet in sheet_names:
    sheets_data[sheet] = pd.read_excel(file_path, sheet_name=sheet).head()

sheets_data, sheet_names
from scipy.stats import ttest_rel

# Read complete data from each sheet
overall_data = pd.read_excel(file_path, sheet_name='Sheet1')
ca_data = pd.read_excel(file_path, sheet_name='CA')
fa_data = pd.read_excel(file_path, sheet_name='FA')

# Calculate t-test for each dataset
def perform_ttest(data, actual_col, forecast_col):
    actual = data[actual_col]
    forecasted = data[forecast_col]
    t_stat, p_value = ttest_rel(actual, forecasted)
    return t_stat, p_value

# Overall data
overall_t_stat, overall_p_value = perform_ttest(overall_data, 'Actual', 'Adjusted Forecast')

# Corresponding author data
ca_t_stat, ca_p_value = perform_ttest(ca_data, 'Actual CA Publications', 'Forecasted CA Publications')

# First author data
fa_t_stat, fa_p_value = perform_ttest(fa_data, 'Actual FA Publications', 'Forecasted FA Publications')

overall_t_stat, overall_p_value, ca_t_stat, ca_p_value, fa_t_stat, fa_p_value


# In[ ]:




