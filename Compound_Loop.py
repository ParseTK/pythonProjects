print("Welcome to Compound Interest Calculator V2!")
# Error Handle Function
def error_handle(string: str, zero: bool = False) -> float:
    """
    A function that takes a string, checks if zero is allowed
    converts the input to a float
    Checks for numerical errors
    returns a float

    :param string: A prompt for a variable
    :param zero: Allows zero or does not
    :type  string: str, zero: bool
    :return: float value
    """
    while True:
        try:
            fValue = float(input(string)) # float(input("variable dependent prompt"))
            if (zero and fValue < 0) or (not zero and fValue <= 0): # Allows zero, or doesn't allow zero
                print("Error! Enter a positive numeric value!")
            else:
                return fValue # returns input
        except ValueError: # Non Numerical Error
            print("Error! Enter a NUMERIC VALUE!")

# Inputs with Error Handling
fDeposit: float = error_handle("What is the original Deposit: ")
fInterest: float = error_handle("What is the Interest Rate (positive values): ") / 100 # calculates interest rate percentage
iMonths: int = int(error_handle("What is the Number of Months (positive values): "))
fSavings_goal: float = error_handle("What is the Savings Goal (can enter zero but not negative): ", True)

# Declaring iMonth and Constant
iMonth: int = 0 # tracks months -> goal
iCAP: int = (12 + 1)

# Iterates -> Inputted Month -> Calculates New Account Balance -> Updates original deposit
for iNum in range(1, iCAP): # Starts at 1, ends iCap
    fNew_balance =  fDeposit * (1 + fInterest / iMonths ) ** iNum
    print(f"Month {iNum: ^4,.0f} Account Balance is: ${fNew_balance: ,.2f}")

if fSavings_goal != 0 and fNew_balance >= fSavings_goal: # Savings Goal success
    print("You've reached your savings goal!")

fNew_balance: float = 0

while fNew_balance < fSavings_goal:  # Loop -> Goal
    iMonth += 1  # Tracking the Loop / Months
    fNew_balance = fDeposit * (1 + fInterest / iMonths) ** iMonth
    if fNew_balance <= fSavings_goal: # Savings Goal
        print(f"It will take: {iMonth: ^4,.0f} months to reach the goal of ${fSavings_goal: ,.2f}")
