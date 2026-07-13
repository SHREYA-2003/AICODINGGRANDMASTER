import math

n = 10
p = 0.5

def binomial_pmf(n, k, p):
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Calculate probability for k = 2, 3, 4
probability = 0
for k in range(2, 5):
    probability += binomial_pmf(n, k, p)

print("Probability of getting between 2 and 4 heads:", probability)
