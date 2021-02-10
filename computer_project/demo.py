#!/usr/bin/python3
import math
import random
import numpy as np
import matplotlib.pyplot as plt

# Check distribution
random.seed(314156)
nSamples = 100000
dat = []
for i in range(0, nSamples):
  dat.append(2.0 * math.sqrt(random.random()))

nbins = 51
plt.hist(dat, nbins)
x = np.arange(0, 2, 0.01)
y = 2000.0 * x
plt.plot(x, y)
plt.savefig('hist.png')

# Compute walk lengths
N_list = [10, 20, 30, 40, 50, 60, 70, 80]
L = []
for Nstep in N_list:
  random.seed(314156)
  L.append(0.0)
  for i in range(0, nSamples):
    d = 0.0
    for step in range(0, Nstep):
      d += 2.0 * math.sqrt(random.random())
    L[-1] += d
  L[-1] /= float(nSamples)

# Check that walk lengths look reasonable
plt.clf()
plt.plot(N_list, L, linestyle='None', marker=".")

# Fit walk lengths to straight line
out = np.polyfit(N_list, L, 1)
print(out)
x = np.arange(0, 80, 0.1)
p = out[0] * x + out[1]
plt.plot(x, p)
plt.savefig('fit.png')

# Fit walk lengths to generalized power law, L = D * x^alpha
# Expect linear power, alpha=1 --> L ~ x
# TRICK: ln(L) = alpha * ln(x) + ln(D) is now linear
logN = np.log(N_list);
logL = np.log(L);
out = np.polyfit(logN, logL, 1)
print(out)
