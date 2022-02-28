import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
S2 = pd.Series([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])
d = {'a': 1, 'b': 2, 'c': 3}

S0 = pd.Series([1, 2, 3, 4, 5.0], ['a', 'b', 'c', 'd', 'e'])
S4 = S0 + S2 * 3

import sys

sys.getsizeof(S4)
lst = S4.to_list()
sys.getsizeof(lst)
sys.getsizeof(df)

S4.append(pd.Series({'f': 15}))

df1 = df.DataFrame()
d = {'prod_name': pd.Series(['ap', 'ba', 'yablok']), 'price': pd.Series([100, 150.0, 15]),
     'count': pd.Series([30, 40, 90])}
d1 = {'prod_name': pd.Series(['ap', 'ba', 'yablok'], index=['v1', 'v2', 'v3']),
      'price': pd.Series([100, 150.0, 15], index=['v1', 'v2', 'v3']),
      'count': pd.Series([30, 40, 90], index=['v1', 'v2', 'v3'])}
df2 = pd.DataFrame(d)
df3 = pd.DataFrame(d1)
df3.iloc[1]
df3.loc['v1']
df3[df3['count'] > 50]
df[df['MonthlyIncome'].isnull()]
df[~df['MonthlyIncome'].isnull()]

df_['DebtRatio'] = df_['DebtRatio'] * df_['MonthlyIncome']  # ругается
df_.loc[df_.index]['DebtRatio'] = df_['DebtRatio'] * df_['MonthlyIncome']  # не ругается
df.loc[df_.index]

df = pd.read_csv('data.csv')
df.fillna({'MonthlyIncome': 1}, inplace=True)
df['DebtRatio'] = df['DebtRatio'] * df['MonthlyIncome']

# df['MonthlyIncome'] = df123['MonthlyIncome']
df['MonthlyIncome'] = df123['MonthlyIncome'].fillna(df123['MonthlyIncome'].mean(), inplace=True)
# 8
df['SeriousDlqin2yrs'].groupby(df['NumberOfDependents']).mean()
df['SeriousDlqin2yrs'].groupby(df['NumberRealEstateLoansOrLines']).mean()
print('bye')
