import pandas as pd

data=pd.read_csv("netflix_titles.csv")

print(data.head(5), data.shape)

data_ind = data.set_index("country")

print(data_ind)








