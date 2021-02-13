#!/usr/bin/python3
import math
import random
import numpy as np
import matplotlib.pyplot as plt

# Check versions
from platform import python_version
print(python_version())
print(np.__version__)
import matplotlib
print(matplotlib.__version__)

# Check distribution
random.seed(42)
nSamples = 100000
dat = []
vev = 0.0
vevSq = 0.0
for i in range(0, nSamples):
  dat.append(2.0 * math.sqrt(random.random()))
  vev += dat[-1]
  vevSq += dat[-1] * dat[-1]

vev /= nSamples
vevSq /= nSamples
print("mu =", vev)
print("sigma =", math.sqrt(vevSq - vev*vev))

nbins = 51
plt.hist(dat, nbins, density=True)
x = np.arange(0, 2, 0.01)
y = 0.5 * x
plt.plot(x, y)
plt.show()
#plt.savefig('hist.png')

# Compute walk lengths
N_list = [10, 20, 30, 40, 50, 60, 70, 80]
L = []
print("N  L")
for Nstep in N_list:
  L.append(0.0)
  for i in range(0, nSamples):
    d = 0.0
    for step in range(0, Nstep):
      d += 2.0 * math.sqrt(random.random())
    L[-1] += d
  L[-1] /= float(nSamples)
  print(Nstep, L[-1])

# Check that walk lengths look reasonable
plt.plot(N_list, L, linestyle='None', marker=".")
plt.show()

# Fit walk lengths to straight line, L = a * N + b
output = np.polyfit(N_list, L, 1)
a=output[0]
b=output[1]
print("a =", a)
print("b =", b)

plt.plot(N_list, L, linestyle='None', marker=".")
x = np.arange(0, 80, 0.1)
p = a * x + b
plt.plot(x, p)
plt.show()
#plt.savefig('fit.png')

# Fit walk lengths to generalized power law, L = c * N^alpha
# Expect linear power, alpha=1 --> L ~ N
# TRICK: log(L) = alpha * log(N) + log(c) is now linear
logN = np.log(N_list);
logL = np.log(L);
output = np.polyfit(logN, logL, 1)
alpha = output[0]
c=np.exp(output[1])
print("alpha =", alpha)
print("c =", c)

plt.plot(N_list, L, linestyle='None', marker=".")
x = np.arange(0, 80, 0.1)
p = c * x**alpha
plt.plot(x, p)
plt.show()
