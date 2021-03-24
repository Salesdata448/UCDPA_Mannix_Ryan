import matplotlib.pyplot as plt
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns

# Importing both Applestore.csv and Applestore_desc csv.Naming Applestore.csv df and Applestore_desc
# df_desc. From df, dropping unwanted columns. Rubric asks to drop duplicates but dropping columns as you can see from
# line 18 there are no missing values or duplicates to drop. Printing head of df to understand data

data = pd.read_csv('AppleStore.csv')
df=data
df=df.drop(['Unnamed: 0','track_name','currency','ver','vpp_lic'],axis=1)
df_desc=pd.read_csv('appleStore_description.csv')
print(df.head())
print(df.shape)

#checking to see if there are missing values

missing_values_count = df.isnull().sum()
print(missing_values_count[0:5])

missing_values_count_df_desc = df_desc.isnull().sum()
print(missing_values_count_df_desc[0:5])
#no missing values in either source but have checked as per rubric instructions.


# columns have been dropped and shape is displayed in shell

# printing types of data for each column. Mixture of floats and integers.

print(df.dtypes)

#getting mean user ratings by indexing by prime genre and getting the mean of user ratings per genre.
mean_user_ratings=df.groupby('prime_genre')['user_rating'].mean().reset_index().sort_values(by=['user_rating'])

plt.figure(figsize = (10, 8), facecolor = None)
sns.set_style("ticks")
plot = sns.barplot(x="prime_genre", y="user_rating", data=mean_user_ratings,order=mean_user_ratings['prime_genre'])

plot.set_xticklabels(mean_user_ratings['prime_genre'], rotation=90, ha="center")
plot.set(xlabel='App prime genre',ylabel='Average user ratings')
plot.set_title('App Genre vs Average User rating')

plt.show()

# I want to work out which is the most popular genre of app in terms of amount of apps in the
# app store

app_count=df["prime_genre"].value_counts().reset_index()

plt.figure(figsize = (10, 8), facecolor = None)
sns.set_style("darkgrid")
plot1 = sns.barplot(x="index", y="prime_genre", data=app_count)

plot1.set_xticklabels(app_count['index'], rotation=90, ha="center")
plot1.set(xlabel='App prime genre',ylabel='App count in App store')
plot1.set_title('App Genre vs App Count')

plt.show()

#pivot table to show mean price and median price per genre.

import numpy as np

mean_price_by_genre = df.pivot_table(values="price", index="prime_genre", aggfunc=[np.mean, np.median])
print(mean_price_by_genre)

print(df)

#As per rubric indexing df by prime_genre, then subsetting with .loc on the expensive genres of apps which are
# business and medical.

df_index = df.set_index("prime_genre")
print(df_index)

Expensive = ["Business", "Medical"]
print(df_index.loc[Expensive])

#slicing by index values by first sorting df_index then slicing using.loc by prime_genre.
df_index_srt = df_index.sort_index()


print(df_index_srt.loc["Book": "Education"])

#Loop over dataframe using iterrows()

df = pd.read_csv('AppleStore.csv', index_col=0)

for lab, row in df.iterrows() :
    print(lab)
    print(row)


#Merging applestore & applestore_desc on "id" as the number uniquely identifies the apps across both
#dataframes. Gives 7197 rows x 19 columns

df_merge = df.merge(df_desc, on='id')

print(df_merge)

import numpy as np

#creating list of prices

list_of_price = df['price'].to_list()
print('price: ', list_of_price)
print('Type of price: ', type(list_of_price))

np_list_of_price = np.array(list_of_price)
print(type(np_list_of_price))

df_index["price"].hist()
plt.show()

print(df_index.head())

#creating bar plot form df_index showing user rating by prime genre

df_rated_by_genre_user_rating = df_index.groupby("prime_genre")["user_rating"].sum()
df_rated_by_genre_user_rating.plot(kind="bar")
plt.show()

#creating scatter plot from df
df_price_user_rating = df.plot(x="price", y="user_rating", kind="scatter", title="Price v Rating")
plt.show()

#charting price and genres
df_chart = pd.read_csv("AppleStore.csv", index_col=6)
fig, ax = plt.subplots()
ax.scatter(df_chart.index, df_chart["prime_genre"])
ax.set_xlabel("Price")
ax.set_ylabel("App Genres")
plt.show()

#scatter plot

fig, ax = plt.subplots()
ax.scatter(df["user_rating"], df["price"])
ax.set_xlabel("User Rating")
ax.set_ylabel("Cost of App")
plt.show()

#App genre vs Total ratings
tot_ratings=df.groupby('prime_genre')['rating_count_tot'].sum().reset_index().sort_values(by=['rating_count_tot'])
tot_ratings
plt.figure(figsize = (10, 8), facecolor = None)
sns.set_style("darkgrid")
plot1 = sns.barplot(x="prime_genre", y="rating_count_tot", data=tot_ratings)
plot1.set_xticklabels(tot_ratings['prime_genre'], rotation=90, ha="center")
plot1.set(xlabel='App prime genre',ylabel='Total ratings')
plot1.set_title('App Genre vs Total ratings')
plt.show()


#App genre vs Content rating
df['cont_rating'] = df.apply(lambda row: row['cont_rating'][:-1], axis=1)
df['cont_rating'] = pd.to_numeric(df['cont_rating'])
avg_cont_ratings=df.groupby('prime_genre')['cont_rating'].mean().reset_index().sort_values(by=['cont_rating'])
avg_cont_ratings
plt.figure(figsize = (10, 8), facecolor = None)
sns.set_style("darkgrid")
plot1 = sns.barplot(x="prime_genre", y="cont_rating", data=avg_cont_ratings)
plot1.set_xticklabels(avg_cont_ratings['prime_genre'], rotation=90, ha="center")
plot1.set(xlabel='App prime genre',ylabel='Content Rating')
plot1.set_title('App Genre vs Content rating')
plt.show()