import scipy.stats as stats

# Parameters
n = 10
p = 0.5

# Probability of at least 7 heads (X >= 7)
# Using survival function (1 - CDF) at 6
prob_win = 1 - stats.binom.cdf(6, n, p)

# Or using PMF sum
prob_win_alt = sum(stats.binom.pmf(k, n, p) for k in range(7, n+1))

print(f"Probability of winning (at least 7 heads): {prob_win:.6f}")
print(f"Same via PMF sum: {prob_win_alt:.6f}")
print(f"As percentage: {prob_win * 100:.2f}%")