import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np

df = pd.read_csv(r"C:\Users\cphar\.Neo4jDesktop\relate-data\dbmss\dbms-92f6f9c7-27e7-4e1f-b517-5760b2f2c472\import\heatmap.csv")

# Pivot the data to form a matrix
heatmap_data = df.pivot(index='State', columns='Sector', values='Amount')

# Plot the heatmap
plt.figure(figsize=(18, 10))
sns.heatmap(heatmap_data, linewidths=0.5, annot=True, fmt='.0f', norm=LogNorm())

plt.title('Total Industry Sector Donations by State')
plt.xlabel('Industry Sector')
plt.ylabel('State')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
