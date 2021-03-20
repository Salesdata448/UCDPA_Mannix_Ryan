import pandas as pd

data=pd.read_csv("netflix_titles.csv")

print(data.shape)

missing_val=data.isnull().sum()

print(missing_val)

new_data = data.dropna(subset=["rating","date_added"])

print(new_data.shape)

new_data = data.drop_duplicates(subset=["director", "rating","duration","date_added"])

print(new_data.shape)









