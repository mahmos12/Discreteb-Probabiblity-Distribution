import scipy.stats as stats

# Parameters
n = 5
p = 2/3

# a) All 5 alive
prob_all = stats.binom.pmf(5, n, p)

# b) At least 3 alive
prob_at_least_3 = 1 - stats.binom.cdf(2, n, p)

# c) Exactly 2 alive
prob_exactly_2 = stats.binom.pmf(2, n, p)

# Display results
print("Exercise 2 - Insurance (5 people)")
print(f"a) P(all 5 alive) = {prob_all:.6f}  ≈ {prob_all * 100:.2f}%")
print(f"b) P(at least 3 alive) = {prob_at_least_3:.6f}  ≈ {prob_at_least_3 * 100:.2f}%")
print(f"c) P(exactly 2 alive) = {prob_exactly_2:.6f}  ≈ {prob_exactly_2 * 100:.2f}%")
print("\n--- Details (optional) ---")
# Show PMF for all k
for k in range(n + 1):
    prob_k = stats.binom.pmf(k, n, p)
    print(f"P(X = {k}) = {prob_k:.6f}")