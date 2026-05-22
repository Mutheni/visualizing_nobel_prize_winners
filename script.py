# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Start coding here!
df = pd.read_csv('data/nobel.csv')
print(df.head())
df.shape
df.info()
print(df.columns.tolist())

## QUESTION ONE -- What is the most commonly awarded gender and birth country?
top_gender = df['sex'].value_counts().index[0]
top_country = df['birth_country'].value_counts().index[0]

print(top_gender)
print(top_country)

### QUESTION TWO -- Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
## Extract the decade from the year column
df['decade'] = (df['year'] // 10) * 10

## Count US-born winners
us_winners = df[df['birth_country'] == "United States of America"]
print(us_winners.shape)

# Total winners per decade
total_per_decade = df.groupby('decade').size()
print(total_per_decade)

# US winners per decade
us_per_decade = df[df['birth_country'] == "United States of America"].groupby('decade').size()
print(us_per_decade)

# ratio
ratio = us_per_decade/total_per_decade.index[0]

# highest ratio 
max_decade_usa = ratio.idxmax()
print(max_decade_usa)


##QUESTION THREE -- Which decade and Nobel Prize category combination had the highest proportion of female laureates?
# Filter female winners
female_winners = df[df['sex']== "Female"]

# Female winners per decade and category
female_group = female_winners.groupby(['decade','category']).size()

# Total winners per decade and category
total_group = df.groupby(['decade','category']).size()

# Ratio
ratio = (female_group / total_group).fillna(0)

# Highest combination
top_combination = ratio.idxmax()
max_female_dict = {top_combination[0]:top_combination[1]}
print(max_female_dict)

## QUESTION FOUR -- Who was the first woman to receive a Nobel Prize, and in what category?
first_woman = female_winners.sort_values('year').iloc[0]

first_woman_name = first_woman['full_name']
first_woman_category = first_woman['category']

print(first_woman_name)
print(first_woman_category)


## Which individuals or organizations have won more than one Nobel Prize throughout the years?
repeat_winners = df.groupby("full_name").size()
repeat_winners = repeat_winners[repeat_winners > 1]
repeat_list = list(repeat_winners.index)
print(repeat_list)
