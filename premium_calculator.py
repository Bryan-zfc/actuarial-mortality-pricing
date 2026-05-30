import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



# assurance assumptions
age = 40
term = 20
benefit = 100000
i = 0.04

# Discount Rate and Monthly interests 
v= (1/1+i)
i_month = (1 + i)**(1/12) - 1
v_month = 1 / (1 + i_month)

#initial expense
initial_expense_fixed = 200

# initial expense as e.g. 50% of first monthly premium
initial_expense_percent = 0.50

# renewal expense as e.g. 5% of every monthly premium
renewal_expense_percent = 0.05



# synthetic mortality rates 
ages = np.arange(30, 150)
qx = 0.0002 * np.exp(0.08 * (ages - 30))
mortality = dict(zip(ages, qx))

#approximate monthly mortality using constant force assumptions
def monthly_q(q_annual):
    return 1 - (1 - q_annual)**(1/12)



# EPV of benefits
epv_benefits = 0
survival = 1
for t in range(term * 12):

    current_age = age + t // 12

    q_m = monthly_q(mortality[current_age])

    death_prob = survival * q_m

    epv_benefits += (
        benefit* (v_month ** (t + 1)) * death_prob
    )

    survival *= (1 - q_m)

# EPV of premium annuity

annuity = 0
survival = 1

for t in range(term * 12):

    current_age = age + t // 12

    q_m = monthly_q(mortality[current_age])

    annuity += (
        (v_month ** t)
        * survival
    )

    survival *= (1 - q_m)


# Gross premium equation

# We have P*EPV(annuity) = EPV(Benefits) + EPV(expenses)

P = (
    epv_benefits + initial_expense_fixed
) / (
    annuity
    - initial_expense_percent
    - renewal_expense_percent * annuity
)


# Results
print(f"EPV of benefits: ${epv_benefits:,.2f}")

print(f"Premium annuity factor: {annuity:.4f}")

print(f"Monthly gross premium: ${P:,.2f}")


# Compute the premiums for a n-year term assurance by age
premium_list = []

for age in range(20, 81):

    epv = 0
    
    for t in range(term):

        q = qx[age + t]
        
        surv = np.prod([
            1 - qx[age + j]
            for j in range(t)
        ])

        epv += (v ** (t+1)) * surv * q

    premium = 100000 * epv

    premium_list.append(premium)

plt.plot(range(20,81), premium_list)

plt.xlabel("Age")
plt.ylabel("Net Single Premium")

plt.title("20-Year Term Insurance Premium by Age")

plt.grid(True)

plt.show()