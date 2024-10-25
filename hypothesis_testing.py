import scipy.stats as stats

# Given data
sample_mean = 3050  
X_mean = 600 
n = 25  
alpha = 0.05  

theoretical_mean = 1000 + 5 * X_mean  
print(f"Theoretical Mean Weekly Cost: {theoretical_mean}")

std_dev = 5 * 25 
print(f"Standard Deviation: {std_dev}")

t_statistic = (sample_mean - theoretical_mean) / (std_dev / (n ** 0.5))
print(f"Test Statistic (t): {t_statistic}")

critical_value = stats.norm.ppf(1 - alpha)
print(f"Critical Value (Z) at alpha = {alpha}: {critical_value}")

if t_statistic > critical_value:
    decision = "Reject the null hypothesis."
else:
    decision = "Fail to reject the null hypothesis."

print("\nDecision:", decision)

if decision == "Reject the null hypothesis.":
    conclusion = "There is strong evidence to support the restaurant owners' claim that the weekly operating costs are higher than the model suggests."
else:
    conclusion = "There is not enough evidence to support the restaurant owners' claim."

print("\nConclusion:", conclusion)
