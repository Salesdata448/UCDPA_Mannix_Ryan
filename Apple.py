import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn')
sns.set(font_scale=1.8)

#read both csv's the description and the data
df_app = pd.read_csv('AppleStore.csv')
df_description = pd.read_csv('appleStore_description.csv')

print(df_app.isnull().sum())

print(df_description.head())

# Merge datasets

df_app['app_desc'] = df_description['app_desc']

df_app = df_app.iloc[:, 1:]

print(df_app.head())

df_app['size_bytes_in_MB'] = df_app['size_bytes'] / (1024 * 1024.0)

df_app['isNotFree'] = df_app['price'].apply(lambda x: 1 if x > 0 else 0)

df_app['isNotFree'].value_counts().plot.bar()
plt.xlabel('IsNotFree(Free == 0, NotFree == 1)')
plt.ylabel('No. of Apps')
plt.show()

