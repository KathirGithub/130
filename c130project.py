import pandas as pd
#read csv file
df = pd.read_csv("dwarf_stars.csv")
#check number of rows and columns
print(df.shape)

del df['luminosity']

df.describe()

df.info()

df.dtypes()

#Save the data into main.csv
df.to_csv('final_data.csv')