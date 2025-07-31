import pandas as pd
import matplotlib.pyplot as plt

# Load dataset and skip the first 4 metadata rows
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)

# Display the first few rows to understand the structure (optional)
print(df.head())

# Extract relevant columns: Country Name and 2022 data
df_2022 = df[['Country Name', '2022']].dropna()

# Get the top 7 countries by population in 2022
top7 = df_2022.sort_values(by='2022', ascending=False).head(7)

# Plotting the bar graph
plt.figure(figsize=(10, 6))
plt.bar(top7['Country Name'], top7['2022'], color='teal')
plt.xlabel("Country")
plt.ylabel("Population in 2022")
plt.title("Top 7 Most Populous Countries (2022)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
