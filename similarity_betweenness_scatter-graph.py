import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

df = pd.read_csv(r"C:\Users\cphar\.Neo4jDesktop\relate-data\dbmss\dbms-92f6f9c7-27e7-4e1f-b517-5760b2f2c472\import\between_sim_export.csv")

sizes = df['contribution_totals'] / 1000000

scatter = plt.scatter(
    x=df['candidate_betweenness'],
    y=df['similarity_avg'],
    s=sizes,
    c=df['Party'],
    cmap='tab10',
    alpha=0.7,
    edgecolors='w',
    linewidth=0.5
)

party_mapping = {
    1: "Republican",
    2: "Democrat",
    3: "Third Party",
    4: "Independent",
    5: "Unknown",
    6: "Libertarian"
}

plt.xlabel('candidate_betweenness')
plt.ylabel('similarity_avg')
plt.title('Scatter plot sized by contribution_totals, colored by Party')

legend_elements = [
    Patch(facecolor=plt.cm.tab10(i-1), edgecolor='w', label=name)
    for i, name in party_mapping.items()
    if i in df['Party'].values  # Only include if present in data
]
plt.legend(handles=legend_elements, title="Party")

plt.show()