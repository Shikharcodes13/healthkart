import pandas as pd
import numpy as np

df = pd.read_excel('Active Users Data - Internship Round 1 Assignment Healthkart.xlsx')

print('=== DATASET STRUCTURE ===')
print(f'Total rows: {len(df)}')
print(f'Total columns: {len(df.columns)}')
print(f'Week columns (w1-w56): {[col for col in df.columns if col.startswith("w")]}')

print('\n=== UNDERSTANDING DATA FORMAT ===')
print('Each row appears to represent a user activity pattern across 56 weeks')
print('Each cell (w1, w2, etc.) contains a user ID that was active in that week\n')

print('=== SAMPLE ANALYSIS ===')
print('First 3 rows, first 10 weeks:')
print(df.iloc[:3, :10])

print('\n=== WEEKLY ACTIVE USERS (WAU) ===')
week_cols = [f'w{i}' for i in range(1, 57)]
wau_counts = {}
for col in week_cols:
    if col in df.columns:
        wau_counts[col] = df[col].notna().sum()

print('Weekly Active Users count:')
for week, count in list(wau_counts.items())[:10]:
    print(f'{week}: {count} users')
print(f'... (showing first 10 of {len(wau_counts)} weeks)')

print('\n=== DATA INSIGHTS ===')
print(f'Average WAU: {np.mean(list(wau_counts.values())):.0f}')
print(f'Min WAU: {min(wau_counts.values())}')
print(f'Max WAU: {max(wau_counts.values())}')


