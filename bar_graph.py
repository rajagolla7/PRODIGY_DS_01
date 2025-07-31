# Task-01: Bar Chart and Histogram Visualization
# Prodigy InfoTech Data Science Internship
# GitHub: https://github.com/Prodigy-InfoTech/data-science-datasets/tree/main/Task%201

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
url = 'https://raw.githubusercontent.com/Prodigy-InfoTech/data-science-datasets/main/Task%201/dataset.csv'
df = pd.read_csv(url)

# Print first few rows
print("Sample data preview:")
print(df.head())

# Histogram for Age distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=10, kde=True, color='steelblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.savefig('age_distribution.png')  # Save as image
plt.show()

# Bar chart for Gender distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Gender', palette='Set2')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.grid(True, axis='y')
plt.tight_layout()
plt.savefig('gender_distribution.png')  # Save as image
plt.show()
