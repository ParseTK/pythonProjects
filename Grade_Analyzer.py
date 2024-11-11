# Welcome and Name entry
print("Welcome to Grade Analyzer!")
name: str = input("Enter Your Name: ")

# Test scores input
iScore1: int = int(input("Enter Test score #1: "))
iScore2: int = int(input("Enter Test score #2: "))
iScore3: int = int(input("Enter Test score #3: "))
iScore4: int = int(input("Enter Test score #4: "))

# Input error check for negative values
if iScore1 < 0 or iScore2 < 0 or iScore3 < 0 or iScore4 < 0:
    print("Test scores must be greater or equal to 0.")
    exit()

# Option to drop the lowest grade
sDrop_option: str = input("Do you want to drop the lowest grade? Enter Y or N: ").lower()

# Lowest score variables
divisor: float = 4.0  # Default
lowest_score: int = 0

# Calculates and drop the Lowest Score
if sDrop_option == "y":
    divisor: float = 3.0  # Change divisor to 3 since we're dropping the lowest score
    lowest_score = min(iScore1, iScore2, iScore3, iScore4)  # Find the lowest score

# Calculates Average Score
average_score: float = (iScore1 + iScore2 + iScore3 + iScore4 - lowest_score) / divisor


def get_grade(num_grade) -> str:
    """
    Converts a numeric grade to a letter grade with possible '+' or '-'

    :param num_grade: Numeric grade
    :return: Letter grade
    """
    digit: int = int(num_grade / 10)

    # Determine the letter grade
    if digit >= 9:
        grade = "A"
    elif digit == 8:
        grade = "B"
    elif digit == 7:
        grade = "C"
    elif digit == 6:
        grade = "D"
    else:
        grade = "F"

    # Add '+' or '-' for grades above 60
    if num_grade > 60:
        digit: int = int(num_grade % 10)
        if num_grade >= 100 or digit >= 7:
            grade += "+"
        elif digit <= 3:
            grade += "-"
    return grade


# Get the final letter grade
sGrade: str = get_grade(average_score)

# Output
print(f"{name}, your average score is {average_score:.2f} your letter grade is {sGrade}.")