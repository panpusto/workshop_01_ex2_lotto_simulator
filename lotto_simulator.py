import random


def get_user_number():
    """Give number from user.

    Try until user give a proper number"""
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number!")

    return result


def get_six_numbers():
    """Get 6 different numbers between 1 and 49. """
    result = []
    while len(result) < 6:
        number = get_user_number()
        if number not in result and 0 < number <= 49:
            result.append(number)

    return result


def print_number_in_order(numbers):
    """Display given numbers in ascending order."""
    print(", ".join(str(number) for number in sorted(numbers)))


def drawing_numbers():
    """Choose 6 random numbers."""
    numbers = list(range(1, 49))
    random.shuffle(numbers)
    return numbers[:6]


def lotto():
    """Main function"""
    user_numbers = get_user_number()
    print("Your numbers:")
    print_number_in_order(user_numbers)

    random_numbers = drawing_numbers()
    print("Lotto numbers:")
    print_number_in_order(random_numbers)

    hits = 0
    for number in user_numbers:
        if number in random_numbers:
            hits += 1

    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == '__main__':
    lotto()
