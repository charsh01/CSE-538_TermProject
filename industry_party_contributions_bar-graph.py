import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv(r"C:\Users\cphar\.Neo4jDesktop\relate-data\dbmss\dbms-92f6f9c7-27e7-4e1f-b517-5760b2f2c472\import\party_industry_distribution.csv")

df = df[df['party'].isin(['Democratic Party', 'Republican Party'])]

pivot_df = df.pivot(index="industry", columns="party", values="total_amount")

ax = pivot_df.plot(kind="bar", figsize=(14, 8))

ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))

for container in ax.containers:
    for bar in container:
        height = bar.get_height()
        x = bar.get_x() + bar.get_width() / 2
        industry = bar.get_label()
        industry_idx = int(round(x))
        industry_label = ax.get_xticklabels()[industry_idx].get_text()
        row = pivot_df.loc[industry_label]
        total = row.sum()
        pct = (height / total) * 100 if total else 0
        ax.text(x, height, f"{pct:.1f}%", ha='center', va='bottom', fontsize=8, rotation=0)


plt.yscale('log')
plt.title("Contributions by Industry and Party")
plt.ylabel("Total Amount")
plt.xlabel("Industry")
plt.xticks(rotation=45, ha='right')
plt.legend(title="Party")
plt.tight_layout()

plt.show()
