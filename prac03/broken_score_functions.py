import random


def main():
    score = float(input("Enter score: "))
    print(determine_status(score))
    print(determine_random(r_number))


r_number = random.randint(0, 100)
print(r_number)


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def determine_random(r_number):
    if r_number < 0 or r_number > 100:
        return "Invalid score"
    elif r_number >= 90:
        return "Excellent"
    elif r_number >= 50:
        return "Passable"
    else:
        return "Bad"
main()
