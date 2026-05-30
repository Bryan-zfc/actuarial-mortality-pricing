import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

ages = np.arange(30, 91)

# synthetic mortality rates
qx = 0.0002 * np.exp(0.08 * (ages - 30))

df = pd.DataFrame({
    "Age": ages,
    "qx": qx
})

def gompertz(x, A, B):
    return A * np.exp(B * x)

log_qx = np.log(qx)

# linear fit
B_fit, logA_fit = np.polyfit(ages, log_qx, 1)

A_fit = np.exp(logA_fit)

print("A =", A_fit)
print("B =", B_fit)

# fitted curve
qx_fit = A_fit * np.exp(B_fit * ages)

print("A =", A_fit)
print("B =", B_fit)

qx_fit = gompertz(ages, A_fit, B_fit)

plt.figure(figsize=(8,5))
plt.plot(ages, qx, label="Observed")
plt.plot(ages, qx_fit, label="Gompertz Fit")
plt.xlabel("Age")
plt.ylabel("Mortality Rate")
plt.title("Mortality Model Fit")
plt.legend()
plt.grid(True)
plt.show()