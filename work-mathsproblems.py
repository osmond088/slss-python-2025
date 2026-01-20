# Math Problems
# Author: Osmond f

# Question 1
def question1():
    print("QUESTION 1: Age in 2049")
    # Get current age from user
    current_age = int(input("How old are you now? "))

    # Calculate age in 2049 (24 years from 2025)
    future_age = current_age + 24

    # Output the result
    print(f"In 2049 you will be {future_age} years old!")
    print()


# QUESTION 2: Olympic Judging
def question2():
    print("QUESTION 2: Olympic Judging")
    # Get scores from 5 judges  
    judge1_input = input("Judge 1: ")
    judge1 = float(judge1_input) if judge1_input else 0.0

    judge2_input = input("Judge 2: ")
    judge2 = float(judge2_input) if judge2_input else 0.0

    judge3_input = input("Judge 3: ")
    judge3 = float(judge3_input) if judge3_input else 0.0

    judge4_input = input("Judge 4: ")
    judge4 = float(judge4_input) if judge4_input else 0.0

    judge5_input = input("Judge 5: ")
    judge5 = float(judge5_input) if judge5_input else 0.0

    # Calculate average
    average = (judge1 + judge2 + judge3 + judge4 + judge5) / 5

    # Display the result
    print(f"Your Olympic score is {average}")
    print()


# QUESTION 3: McDonald's Order
def question3():
    print("QUESTION 3: McDonald's Order")
    # Initialize total
    total = 0

    # Ask about burger
    burger_response = input("Would you like a burger for $5? (Yes/No)\n")
    if burger_response.lower() == "yes":
        total += 5

    # Ask about fries
    fries_response = input("Would you like fries for $3? (Yes/No)\n")
    if fries_response.lower() == "yes":
        total += 3

    # Calculate total with 14% tax
    total_with_tax = total * 1.14

    # Display the result
    print(f"Your total is ${total_with_tax}")
    print()


def main():
    # Run all questions
    question1()
    question2()
    question3()


if __name__ == "__main__":
    main()
