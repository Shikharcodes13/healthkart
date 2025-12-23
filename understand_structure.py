import pandas as pd
import numpy as np

df = pd.read_excel('Active Users Data - Internship Round 1 Assignment Healthkart.xlsx')

print('=== UNDERSTANDING DATA STRUCTURE ===\n')

print('Hypothesis 1: Each row is a user, cells show when they were active')
print('Checking first user (row 0):')
first_row = df.iloc[0]
print(f'  User appears in {first_row.notna().sum()} weeks')
print(f'  First 5 weeks: {first_row[:5].tolist()}')

print('\nHypothesis 2: Each cell contains a user ID active that week')
print('Checking if user IDs repeat across rows for same week:')
print(f'  Week 1 (w1) - unique user IDs: {df["w1"].nunique()}')
print(f'  Week 1 (w1) - total non-null entries: {df["w1"].notna().sum()}')

print('\n=== KEY INSIGHT ===')
print('For growth accounting, we need to identify:')
print('1. Users active in each week (WAU)')
print('2. New users (first time active)')
print('3. Retained users (active in previous week + current week)')
print('4. Churned users (active in previous week, not in current)')
print('5. Resurrected users (not active in previous week, but active now)')

print('\n=== Sample: Week 1 vs Week 2 ===')
w1_users = set(df['w1'].dropna().unique())
w2_users = set(df['w2'].dropna().unique())

new_in_w2 = w2_users - w1_users
retained = w1_users & w2_users
churned_from_w1 = w1_users - w2_users
resurrected_in_w2 = w2_users - w1_users

print(f'Week 1 WAU: {len(w1_users)}')
print(f'Week 2 WAU: {len(w2_users)}')
print(f'New in Week 2: {len(new_in_w2)}')
print(f'Retained from Week 1: {len(retained)}')
print(f'Churned from Week 1: {len(churned_from_w1)}')
print(f'Resurrected in Week 2: {len(resurrected_in_w2)}')
print(f'Net Growth: {len(w2_users) - len(w1_users)}')


