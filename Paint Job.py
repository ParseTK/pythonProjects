import math

def get_float_input(string: str) -> float:
    """
    Ensures the value entered is valid

    :param string: The prompt
    :return: float
    """
    while True:
        try:
            value: float = float(input(string))
            if value <= 0:
                print("Error! Enter a positive numeric value!")
            else:
                return value  # returns input
        except ValueError:  # Non Numerical Error
            print("Error! Enter a NUMERIC VALUE!")

def get_gallon_paint(area: float, gallon: float) -> int:
    """

    Gets the number of gallons needed.

    :param area: The area of the gallon.
    :param gallon: The number of gallons.
    :return: int
    """
    num_paint: int =  math.ceil(area / gallon)

    return int(num_paint)

def get_labor_hours(time: float, area: float, gallon: float) -> float:
    """
    Gets the number of labor hours

    :param gallon:
    :param area:
    :param time: The time in hours
    :return: float: The number of labor hours
    """
    labor_time: float = time * get_gallon_paint(area, gallon)

    return labor_time

def get_labor_cost(cost: float, time: float, area: float, gallon: float) -> float:
    """
    Gets the cost of labor

    :param gallon:
    :param area:
    :param time:
    :param cost: Price per hour
    :return: float: The cost of labor
    """
    labor_cost: float = get_labor_hours(time, area, gallon) * cost
    return labor_cost

def get_paint_cost(paint_cost: float, area: float, gallon: float) -> float:
    """
    Gets the total cost of paint

    :param gallon:
    :param area:
    :param paint_cost: Price per gallon of paint
    :return: float: The total cost of paint
    """

    p_cost = get_gallon_paint(area, gallon) * paint_cost

    return p_cost

def get_sales_tax(state: str) -> float:
    """
    Returns the tax rate for the passed in state variable as follows:
     If the state is CT the tax rate is .06
     If the state is MA the tax rate is .0625
     If the state is ME the tax rate is .085
     If the state is RI the tax rate is .07
     If the state is VT the tax rate is .06
     None of the above tax rate is 0.

    :param state: state input
    :return: Tax rate
    """
    # Conditions
    if state == "CT" or state == "VT":
        return .06
    elif state == "MA":
        return .0625
    elif state == "ME":
        return .085
    elif state == "RI":
        return .07
    else:
        return 0

def show_cost_estimate(area, gallon, time, cost, paint_cost, state, name) -> None:
    """
    Calculates the details, cost estimate, and creates a file for the job.

    :return:
    """
    square_ft: int = int(get_gallon_paint(area, gallon)) # area, gallon
    hours_labor: float = get_labor_hours(time, area, gallon) # fLabor
    cost_labor: float = get_labor_cost(cost, time, area, gallon) # fCost_hour
    cost_paint: float = get_paint_cost(paint_cost, area, gallon) # fPaint_price
    tax_rate: float = get_sales_tax(state) # sState
    labor_costs: float = cost_labor + cost_paint
    tax: float = tax_rate * labor_costs
    total: float = labor_costs + tax

    # Output
    print(f"gallons of paint: {square_ft: ,.0f}")
    print(f"Hours of labor: {hours_labor: ,.0f}")
    print(f"Paint charges: ${cost_paint: ,.2f}")
    print(f"Labor charges: ${cost_labor: ,.2f}")
    print(f"Tax: ${tax: ,.2f}")
    print(f"Total cost: ${total: ,.2f}")

    # Creates a file and writes to it
    f = open(f"{name}_PaintJobOutput.txt", "w")
    f.write(f"{name}'s Paint Job Details\n")
    f.write(f"gallons of paint: {square_ft: ,.0f}\n")
    f.write(f"Hours of labor: {hours_labor: ,.0f}\n")
    f.write(f"Paint charges: ${cost_paint: ,.2f}\n")
    f.write(f"Labor charges: ${cost_labor: ,.2f}\n")
    f.write(f"Tax: ${tax: ,.2f}\n")
    f.write(f"Total cost: ${total: ,.2f}\n")
    f.close()

def main() -> None:  # contains the logic
    fWall_area: float = float(get_float_input("What is the square feet of the wall: "))
    fPaint_price: float = float(get_float_input("What is the price of the paint: "))
    fFeet_gallon: float = float(get_float_input("How many feet per gallon of paint: "))
    fLabor: float = float(get_float_input("How many labor hours per gallon: "))
    fCost_hour: float = float(get_float_input("How much do you charge for labor per hour: "))
    sState: str = input("What State is the job is in? ").upper()
    sName: str = input("What is customers Last Name? ")

    # Calls the function
    show_cost_estimate(fWall_area, fFeet_gallon, fLabor, fCost_hour, fPaint_price, sState, sName)

# Calls main function and outputs the logic
main()
