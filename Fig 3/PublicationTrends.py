#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

# Load the dataset
file_path = 'Final Data CA+FA.csv'
data = pd.read_csv(file_path)

# Filter data for only 'Corresponding' author type
data_corresponding = data[final_data['Author Type'] == 'Corresponding']

# Get the top 20 countries by publication count in the final dataset with 'Corresponding' author type
top_20_data_corresponding = data_corresponding['Country'].value_counts().head(20).reset_index()
top_20_data_corresponding.columns = ['Country', 'Publication Count']

# Display the result
print(top_20_data_corresponding)


# In[4]:


# Calculate the number of unique publications from each country using the 'WOS ID' column
unique_publications_per_country = data.groupby('Country')['WOS ID'].nunique().sort_values(ascending=False)

unique_publications_per_country


# In[6]:


# Extract the top 10 countries based on the number of unique publications
top_10_unique_publications_per_country = unique_publications_per_country.head(15)
top_10_unique_publications_per_country


# In[1]:


import pandas as pd

# Load the data from a CSV file
file_path = 'Final Data CA+FA.csv' 

data = pd.read_csv(file_path)

# Split the data based on the 'Author Type'
first_authors = data[data['Author Type'] == 'First']
corresponding_authors = data[data['Author Type'] == 'Corresponding']

# Calculate counts for male and female authors
first_authors_male = first_authors[first_authors['Gender'] == 'male']['Country'].value_counts()
first_authors_female = first_authors[first_authors['Gender'] == 'female']['Country'].value_counts()
corresponding_authors_male = corresponding_authors[corresponding_authors['Gender'] == 'male']['Country'].value_counts()
corresponding_authors_female = corresponding_authors[corresponding_authors['Gender'] == 'female']['Country'].value_counts()

# Combine the data into DataFrames for easier manipulation
fa_counts = pd.DataFrame({
    'Male First Authors': first_authors_male,
    'Female First Authors': first_authors_female
}).fillna(0).astype(int)

ca_counts = pd.DataFrame({
    'Male Corresponding Authors': corresponding_authors_male,
    'Female Corresponding Authors': corresponding_authors_female
}).fillna(0).astype(int)

# Define top countries including the Netherlands and their specific order
top_countries = [
    "United States of America", "China", "Germany", "Japan", "England",
    "Italy", "Canada", "Spain", "South Korea", "Netherlands", "Sweden"
]

# Filter the DataFrames to include only the specified countries
fa_gender_bifurcation = fa_counts.loc[top_countries]
ca_gender_bifurcation = ca_counts.loc[top_countries]

# Output the gender bifurcation tables for First and Corresponding Authors
print("Gender Bifurcation for First Authors (FA):")
print(fa_gender_bifurcation)
print("\nGender Bifurcation for Corresponding Authors (CA):")
print(ca_gender_bifurcation)


# In[ ]:




