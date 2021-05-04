#!/usr/bin/python3
import random
import time
# ------------------------------------------------------------------
# Compute pi through Monte Carlo importance sampling
random.seed(42)

# Loop over various numbers of samples
for N in [1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9]:
  secs = -time.time()
  count = 0
  for i in range(int(N)):
    x = 2.0 * random.random() - 1.0
    y = 2.0 * random.random() - 1.0
    if (x*x + y*y < 1):
      count += 1

  P = 4.0 * count / N
  secs += time.time()
  print("%.0e samples --> pi=%.6g in %.4g seconds" % (N, P, secs))
# ------------------------------------------------------------------
