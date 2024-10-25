import numpy as np
import pandas as pd
import scipy.stats as stats

data = {
    'Very Satisfied': [50, 70],
    'Satisfied': [80, 100],
    'Neutral': [60, 90],
    'Unsatisfied': [30, 50],
    'Very Unsatisfied': [20, 50]
}

df = pd.DataFrame(data, index=['Smart Thermostat', 'Smart Light'])
print("Observed Frequencies:\n", df)

# Total counts
df.loc['Total'] = df.sum()
df['Total'] = df.sum(axis=1)

n_rows = df.shape[0] - 1  
n_cols = df.shape[1] - 1  
grand_total = df.values.sum()
expected = np.zeros((n_rows, n_cols))

for i in range(n_rows):
    for j in range(n_cols):
        expected[i][j] = (df.iloc[i, -1] * df.iloc[-1, j]) / grand_total

print("\nExpected Frequencies:\n", expected)

observed = df.iloc[:-1, :-1].values  
chi_square_statistic = ((observed - expected) ** 2 / expected).sum()
print("\nChi-Square Statistic:", chi_square_statistic)

alpha = 0.05
df_chi_square = (n_rows - 1) * (n_cols - 1) 
critical_value = stats.chi2.ppf(1 - alpha, df_chi_square)
print("\nCritical Value:", critical_value)

if chi_square_statistic > critical_value:
    decision = "Reject the null hypothesis."
else:
    decision = "Fail to reject the null hypothesis."

print("\nDecision:", decision)
