# actuarial-mortality-pricing
I'm currently studying for actuary exams, so I wanted to implement some pricing for assurances. In this project we explore mortality modelling and life insurance pricing using Australian mortality data.

The analysis includes:

- Mortality rate visualisation
- Gompertz mortality model fitting
- Expected present value of benefits
- Monthly gross premium calculations
- Premium plotted against age and interest rates

All modelling was implemented in Python.

# Key Results

The Gompertz model provides a reasonable approximation to adult mortality between ages 20 and 90. (but seems to slightly overshoot) 

Premiums increase significantly with entry age due to increasing mortality risk. (As expected)

Premiums decrease as interest rates increase because future liabilities are discounted more heavily.
