# Compound interest Calculator FV= PV(1+r/m)**(m*t)

# Inputs:
nPrincipal_invested = float(input("Enter starting principal: "))
nInterest_rate = float(input("Enter the annual interest rate: "))
nCompound = int(input("How many times per year is the interest compounded? "))
nNumber_of_periods = float(input("For how many years will the account earn interest? "))

# Calculations:
nCOMPOUND_BY_PERIODS = nCompound * float(nNumber_of_periods) # (m*t) = mt
nCOMPOUND_RATE = (nInterest_rate / 100) / nCompound + 1 # (1+r/m) nInterest_rate = R, r=R/100
nFUTURE_VALUE = nPrincipal_invested * (nCOMPOUND_RATE) ** nCOMPOUND_BY_PERIODS # FV = PV(nCOMPOUND_RATE)**nCOMPOUND_BY_PERIODS

# Output:
print(f"At the end of {int(nNumber_of_periods)} years you will have ${nFUTURE_VALUE:,.2f}")