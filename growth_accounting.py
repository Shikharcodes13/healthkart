import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('Active Users Data - Internship Round 1 Assignment Healthkart.xlsx')

week_cols = [f'w{i}' for i in range(1, 57)]

results = []

all_users_ever_seen = set()

for i in range(len(week_cols)):
    current_week = week_cols[i]
    
    if current_week not in df.columns:
        continue
    
    current_users = set(df[current_week].dropna().unique())
    wau_current = len(current_users)
    
    if i == 0:
        new_users = current_users
        retained_users = set()
        churned_users = set()
        resurrected_users = set()
        previous_users = set()
    else:
        previous_week = week_cols[i-1]
        previous_users = set(df[previous_week].dropna().unique())
        
        retained_users = current_users & previous_users
        churned_users = previous_users - current_users
        
        users_not_in_previous = current_users - previous_users
        
        new_users = users_not_in_previous - all_users_ever_seen
        resurrected_users = users_not_in_previous & all_users_ever_seen
    
    all_users_ever_seen.update(current_users)
    
    quick_ratio = (len(new_users) + len(resurrected_users)) / len(churned_users) if len(churned_users) > 0 else np.nan
    retention_rate = len(retained_users) / len(previous_users) if len(previous_users) > 0 else np.nan
    
    results.append({
        'Week': i + 1,
        'Week_Label': current_week,
        'WAU': wau_current,
        'New': len(new_users),
        'Retained': len(retained_users),
        'Churned': len(churned_users),
        'Resurrected': len(resurrected_users),
        'Quick_Ratio': quick_ratio,
        'Retention_Rate': retention_rate,
        'Net_Growth': wau_current - (len(previous_users) if i > 0 else wau_current)
    })

results_df = pd.DataFrame(results)

print("=== GROWTH ACCOUNTING RESULTS ===")
print(results_df.to_string())

results_df.to_csv('growth_accounting_results.csv', index=False)
print("\nResults saved to 'growth_accounting_results.csv'")

try:
    plt.style.use('seaborn-v0_8-darkgrid')
except:
    try:
        plt.style.use('seaborn-darkgrid')
    except:
        plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

week_numbers = results_df['Week'].values

ax1 = axes[0, 0]
ax1.bar(week_numbers, results_df['New'], label='New', alpha=0.8, color='#2ecc71')
ax1.bar(week_numbers, results_df['Resurrected'], bottom=results_df['New'], label='Resurrected', alpha=0.8, color='#3498db')
ax1.bar(week_numbers, results_df['Retained'], bottom=results_df['New'] + results_df['Resurrected'], label='Retained', alpha=0.8, color='#9b59b6')
ax1.bar(week_numbers, -results_df['Churned'], label='Churned', alpha=0.8, color='#e74c3c')
ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
ax1.set_xlabel('Week', fontsize=12)
ax1.set_ylabel('Number of Users', fontsize=12)
ax1.set_title('Weekly Growth Accounting Chart', fontsize=14, fontweight='bold')
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)

ax2 = axes[0, 1]
ax2.plot(week_numbers, results_df['WAU'], marker='o', linewidth=2, markersize=4, color='#34495e', label='WAU')
ax2.set_xlabel('Week', fontsize=12)
ax2.set_ylabel('Weekly Active Users', fontsize=12)
ax2.set_title('Weekly Active Users Trend', fontsize=14, fontweight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)

ax3 = axes[1, 0]
ax3.plot(week_numbers[1:], results_df['Quick_Ratio'].values[1:], marker='o', linewidth=2, markersize=4, color='#e67e22', label='Quick Ratio')
ax3.axhline(y=1, color='red', linestyle='--', linewidth=1, label='Break-even (1.0)')
ax3.set_xlabel('Week', fontsize=12)
ax3.set_ylabel('Quick Ratio', fontsize=12)
ax3.set_title('Quick Ratio Trend (New + Resurrected) / Churned', fontsize=14, fontweight='bold')
ax3.legend()
ax3.grid(True, alpha=0.3)

ax4 = axes[1, 1]
ax4.plot(week_numbers[1:], results_df['Retention_Rate'].values[1:] * 100, marker='o', linewidth=2, markersize=4, color='#16a085', label='Retention Rate')
ax4.set_xlabel('Week', fontsize=12)
ax4.set_ylabel('Retention Rate (%)', fontsize=12)
ax4.set_title('Week-over-Week Retention Rate', fontsize=14, fontweight='bold')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('growth_accounting_charts.png', dpi=300, bbox_inches='tight')
print("\nCharts saved to 'growth_accounting_charts.png'")
plt.close()

print("\n=== SUMMARY STATISTICS ===")
print(f"Average WAU: {results_df['WAU'].mean():.0f}")
print(f"Average New Users per week: {results_df['New'].mean():.0f}")
print(f"Average Retained Users per week: {results_df['Retained'].mean():.0f}")
print(f"Average Churned Users per week: {results_df['Churned'].mean():.0f}")
print(f"Average Resurrected Users per week: {results_df['Resurrected'].mean():.0f}")
print(f"Average Quick Ratio: {results_df['Quick_Ratio'].mean():.2f}")
print(f"Average Retention Rate: {results_df['Retention_Rate'].mean()*100:.1f}%")

