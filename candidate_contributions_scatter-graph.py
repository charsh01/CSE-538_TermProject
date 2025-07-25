import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

df = pd.read_csv(r"C:\Users\cphar\.Neo4jDesktop\relate-data\dbmss\dbms-92f6f9c7-27e7-4e1f-b517-5760b2f2c472\import\candidate_contributions_scatter.csv")
cols = ['PartyEnum', 'ContributorCount', 'TotalPACContributions']
df = df[cols]

# Define custom colors for each PartyEnum value
party_colors = {
    1: '#1f77b4',  # Democratic - Blue
    2: '#d62728',  # Republican - Red
    3: '#2ca02c',  # Independent - Green
    4: '#7f7f7f',  # Unknown - Gray
    5: '#9467bd'   # Third Party - Purple
}

party_labels = {
    1: "Democratic Party",
    2: "Republican Party",
    3: "Independent Party",
    4: "Unknown Party",
    5: "Third Party"
}

# Generate list of colors corresponding to each row's PartyEnum
colors = [party_colors.get(p, '#000000') for p in df['PartyEnum']]

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(
    df['ContributorCount'],
    df['TotalPACContributions'],
    c=colors,
    alpha=0.7,
    s=100
)

# Manual legend with fixed party colors
legend_elements = [
    Patch(facecolor=party_colors[k], label=party_labels[k])
    for k in sorted(party_colors)
    if k in df['PartyEnum'].unique()
]
ax.legend(handles=legend_elements, title="Political Party")

# Axes and layout
ax.set_title("Candidate Contributions by Party")
ax.set_xlabel("Contributor Count")
ax.set_ylabel("Total PAC Contributions")
plt.tight_layout()
plt.show()