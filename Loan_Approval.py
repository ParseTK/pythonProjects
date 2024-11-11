print("Welcome to Loan Approval Calculator")

# 50 States in a tuple
STATE_LIST = ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
              "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT",
              "VA", "WA", "WV", "WI", "WY")

def get_input(prompt, validation_fn=None, error_message="Invalid input."):
    while True:
        value = input(prompt)
        if validation_fn and not validation_fn(value):
            print(f"ERROR! {error_message}")
        else:
            return value

def valid_state(state):
    return state.upper() in STATE_LIST

def positive_numeric(value):
    try:
        return float(value) > 0
    except ValueError:
        return False

def non_negative_numeric(value):
    try:
        return float(value) >= 0
    except ValueError:
        return False

def valid_date(value):
    try:
        month, day, year = map(int, value.split('/'))
        return 1 <= month <= 12 and 1 <= day <= 31 and 1900 <= year <= 2100
    except ValueError:
        return False

# Inputs
inputs = {
    "state": get_input("What State do you live in? ", valid_state, "Enter a valid state code."),
    "first_name": get_input("Enter your First name: "),
    "middle_name": get_input("Enter your Middle name: "),
    "last_name": get_input("Enter your Last name: "),
    "dob": get_input("Enter your date of birth (MM/DD/YYYY): ", valid_date, "Enter a valid date (MM/DD/YYYY)."),
    "pin": get_input("What is your four digit pin: ", positive_numeric, "Enter a positive numeric value."),
    "loan_amount": get_input("Enter requested loan amount (minimum 250): ", positive_numeric, "Enter a positive numeric value."),
    "citizen": get_input("Are you a U.S Citizen? "),
    "disabled": get_input("Are you Disabled? "),
    "veteran": get_input("Are you a Veteran? "),
    "employed": get_input("Are you currently employed? "),
    "time_employed": get_input("Enter time at current position: "),
    "income": get_input("Enter yearly income (minimum $10,000): ", positive_numeric, "Enter a positive numeric value."),
    "expenses": get_input("Enter total Monthly Expenses: ", non_negative_numeric, "Enter a non-negative numeric value."),
}

# Loan approval function
def loan_approval(income, expenses, loan_amount) -> bool:
    monthly_income = income / 12
    net_income = monthly_income - expenses
    loan_payment = loan_amount / 12

    return net_income > loan_payment

# Calculate loan approval
income = float(inputs["income"])
expenses = float(inputs["expenses"])
loan_amount = float(inputs["loan_amount"])

# Check if loan is approved
is_approved = loan_approval(income, expenses, loan_amount)
status = "Loan Approved" if is_approved else "Loan Denied"

# Output results
print("\nProfile:")
for key, value in inputs.items():
    print(f"{key.replace('_', ' ').title()}: {value}")

print(f"\nLoan Status: {status}")