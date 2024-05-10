import pandas as pd
#Read a CSV file
data= pd.read_csv("C:/Users/saura/Desktop/DS/data.csv")
print(data)

# Read a JSON FILE = pd.read_json('')

# Removing rows with missing values 
data_cleaned = data.dropna() 

# Displaying the DataFrame after removing missing values 
print("\nDataFrame after removing rows with missing values:") 
print(data_cleaned)

# Sorting , filtering , grouping
sorted_df = df.sort_values(by='Sales', ascending=False)

print(sorted_df)

.......................

filtered_df = df.loc[df['Sales'] > 8000]

print(filtered_df)
..................................................
 
grouped_df = df.groupby('Region')['Sales'].sum()

print(grouped_df)
