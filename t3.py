import scipy.stats as stats

p = 3/75  # probability of defective
k = 6

# Geometric distribution 
prob = (1-p)**(k-1) * p


prob_scipy = stats.geom.pmf(k, p)

print(f"Probability first defective is found on 6th test: {prob:.6f}")
print(f"Using scipy.geom.pmf: {prob_scipy:.6f}")