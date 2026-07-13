import math

lam = 10  # expected number of rainy days

# Poisson PMF
def poisson_pmf(k, lam):
    return (math.exp(-lam) * lam**k) / math.factorial(k)

# 1. P(X >= 12)
p_ge_12 = 0
for k in range(12, 50):  # upper limit large enough
    p_ge_12 += poisson_pmf(k, lam)

# 2. P(12 <= X <= 18)
p_12_to_18 = 0
for k in range(12, 19):
    p_12_to_18 += poisson_pmf(k, lam)

print("P(X >= 12):", p_ge_12)
print("P(12 <= X <= 18):", p_12_to_18)
