import pandas as pd

app_data = pd.read_csv('AppleStore.csv')

print(app_data)
print(app_data.shape)
#Apple dataset imported as csv from Kaggle

missing_val=app_data.isnull().sum

print(missing_val)
#no missing values

#dropping rows where data is missing
droprows=app_data.dropna()
print(app_data.shape,droprows.shape)








