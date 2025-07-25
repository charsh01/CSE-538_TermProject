import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

df = pd.read_csv(r"C:\Users\cphar\.Neo4jDesktop\relate-data\dbmss\dbms-92f6f9c7-27e7-4e1f-b517-5760b2f2c472\import\between_sim_export.csv")

# Scale the candidate dots
sizes = df['contribution_totals'] / 1000000

# Format the dots, most noteably with size and candidate color
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

# Enumerate party for color mapping
party_mapping = {
    1: "Republican",
    2: "Democrat",
    3: "Third Party",
    4: "Independent",
    5: "Unknown",
    6: "Libertarian"
}

# Create labels
plt.xlabel('candidate_betweenness')
plt.ylabel('similarity_avg')
plt.title('Scatter plot sized by contribution_totals, colored by Party')

legend_elements = [
    Patch(facecolor=plt.cm.tab10(i-1), edgecolor='w', label=name)
    for i, name in party_mapping.items()
    if i in df['Party'].values
]
plt.legend(handles=legend_elements, title="Party")

plt.show()
