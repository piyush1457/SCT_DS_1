
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('dataset.csv', skiprows=4)
data = data[['Country Name', '2022']].dropna()
data_sorted = data.sort_values(by='2022', ascending=False).head(20)  
plt.figure(figsize=(12, 6))
plt.barh(data_sorted['Country Name'], data_sorted['2022'], color='red')
plt.xlabel('Labor Force (2022)')
plt.ylabel('Country')
plt.title('Labor Force Distribution by Country (Top 20 in 2022)')
plt.gca().invert_yaxis() 
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['2022'], bins=20, color='green', edgecolor='black')
plt.xlabel('Labor Force Size')
plt.ylabel('Frequency')
plt.title('Distribution of Labor Force Sizes Across Countries (2022)')
plt.show()
