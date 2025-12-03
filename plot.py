import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("ising2d_vs_T.dat")
T = data[:, 0]
M = data[:, 1]
E = data[:, 2]
C = data[:, 3]

idx = np.argsort(T)
T = T[idx]
M = M[idx]
E = E[idx]
C = C[idx]

plt.figure(figsize=(6, 8))

plt.subplot(3, 1, 1)
plt.plot(T, E)
plt.ylabel("E per spin")
plt.title("2D Ising model: E, M, C vs T")

plt.subplot(3, 1, 2)
plt.plot(T, M)
plt.ylabel("M per spin")

plt.subplot(3, 1, 3)
plt.plot(T, C)
plt.xlabel("T")
plt.ylabel("C per spin")

plt.tight_layout()
plt.savefig("ising.pdf")
