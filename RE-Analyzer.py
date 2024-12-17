def get_float_input(prompt: str, num: float) -> float:
    """
    Gets a prompt from a user with dynamic validation (num)

    :param prompt:
    :param num:
    :return:
    """
    while True: # loop for validation
        try:
            sale_price: float = float(input(prompt))
            if sale_price <= num: # dynamic num validation
                print("Error! Enter a positive numeric value!")
            else:
                return sale_price
        except ValueError:
            print("Error! Enter a NUMERIC value!")


def get_median(collection: list) -> float:
    """
    Calculates the median of a list

    :param collection:
    :return:
    """
    sorted_collection: list = sorted(collection) # Sort the list to access the correct median of sales
    len_collection: int = len(sorted_collection) # Length of the sorted list
    if len_collection == 0:
        raise ValueError("The list is empty")

    # Length of the collection is odd
    if len_collection % 2 != 0:
        return float(sorted_collection[len_collection // 2])

    # Length of the collection is even
    else:
        entry1: int = sorted_collection[len_collection // 2]
        entry2: int = sorted_collection[len_collection // 2 - 1] # accesses element before the first middle element
        return (entry1 + entry2) / 2 # returns the average of the two middle elements


def main() -> None:
    """
    Inputs, calculates, and outputs all the data

    :return:
    """
    sale_value: list = []
    while True: # loop for sales input

        value: float = get_float_input("Enter Property Sales Value: ", 0)
        sale_value.append(value) # adds value to sale value list

        while True: # loop for string input

            y_or_n: str = input("Would you like to continue (Y/N) ").lower()
            if y_or_n in ["y", "n"]:
                break # breaks nested loop

        if y_or_n == "n":
            break # breaks loop

    # sorts the list
    sale_value.sort()

    # Iterates through the list, applies a number starting at 1 to each index in the list and outputs it to the console
    for i, value in enumerate(sale_value, start=1):
        print(f"\nProperty {i}. Sale Value: ${value:,.2f}")

    # Declaring variable for min, max, sum and outputs to the console
    min_sale: float = min(sale_value) # Min
    print(f"\nThe Lowest Sale: ${min_sale:,.2f}")
    max_sale: float = max(sale_value) # Max
    print(f"The Highest Sale: ${max_sale:,.2f}")
    total_sale: float = sum(sale_value) # Total
    print(f"The Total Sale: ${total_sale:,.2f}")

    # Declares average variable and outputs it to the console
    sale_average: float = total_sale / len(sale_value)
    print(f"\nSales Average: ${sale_average:,.2f}")

    # Declares a variable of the median sale and outputs it to the console
    median_sale: float = get_median(sale_value)
    print(f"\nThe Median Sale: ${median_sale:,.2f}")

    # Declares a variable of the commission and outputs it to the console
    sale_commission: float = (total_sale * 0.03)
    print(f"\nthe commission: ${sale_commission:,.2f}")

main()
