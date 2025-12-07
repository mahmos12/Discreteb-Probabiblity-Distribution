import scipy.stats as stats

lam = 1  # average failures per 4 months

# a) No failure
prob_0 = stats.poisson.pmf(0, lam)

# b) Exactly 1 failure
prob_1 = stats.poisson.pmf(1, lam)

# c) Exactly 2 failures
prob_2 = stats.poisson.pmf(2, lam)

# d) Exactly 3 failures
prob_3 = stats.poisson.pmf(3, lam)

print("Exercise 4 - Computer failures (Poisson distribution)")
print(f"λ = {lam} failure per 4 months")
print("--------------------------------------------------")
print(f"a) P(0 failures): {prob_0:.6f}  (~{prob_0*100:.2f}%)")
print(f"b) P(1 failure):  {prob_1:.6f}  (~{prob_1*100:.2f}%)")
print(f"c) P(2 failures): {prob_2:.6f}  (~{prob_2*100:.2f}%)")
print(f"d) P(3 failures): {prob_3:.6f}  (~{prob_3*100:.2f}%)")