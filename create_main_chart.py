import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

results_df = pd.read_csv('growth_accounting_results.csv')

fig, ax = plt.subplots(figsize=(18, 10))

week_numbers = results_df['Week'].values[1:]
new = results_df['New'].values[1:]
resurrected = results_df['Resurrected'].values[1:]
retained = results_df['Retained'].values[1:]
churned = results_df['Churned'].values[1:]

bottom_positive = np.zeros(len(week_numbers))
bottom_negative = np.zeros(len(week_numbers))

ax.bar(week_numbers, new, bottom=bottom_positive, label='New Users', 
       color='#2ecc71', alpha=0.85, width=0.6)
bottom_positive += new

ax.bar(week_numbers, resurrected, bottom=bottom_positive, label='Resurrected Users', 
       color='#3498db', alpha=0.85, width=0.6)
bottom_positive += resurrected

ax.bar(week_numbers, retained, bottom=bottom_positive, label='Retained Users', 
       color='#9b59b6', alpha=0.85, width=0.6)
bottom_positive += retained

ax.bar(week_numbers, -churned, bottom=bottom_negative, label='Churned Users', 
       color='#e74c3c', alpha=0.85, width=0.6)
bottom_negative -= churned

ax.axhline(y=0, color='black', linestyle='-', linewidth=1.2)

ax.set_xlabel('Week', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Users', fontsize=14, fontweight='bold')
ax.set_title('Weekly Growth Accounting Chart\n(New + Resurrected + Retained vs Churned)', 
             fontsize=16, fontweight='bold', pad=20)

ax.legend(loc='upper left', fontsize=12, framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle='--', axis='y')

ax.set_xlim(1.5, 56.5)
ax.set_xticks(range(2, 57, 4))
ax.set_xticklabels([f'W{i}' for i in range(2, 57, 4)], rotation=45, ha='right')

plt.tight_layout()
plt.savefig('Weekly_Growth_Accounting_Chart.png', dpi=300, bbox_inches='tight')
print("Main chart saved to 'Weekly_Growth_Accounting_Chart.png'")
plt.close()


