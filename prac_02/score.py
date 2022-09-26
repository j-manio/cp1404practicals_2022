"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """ Determine the user input score """
    score = float(input("Enter score: "))
    print(f'The score {score} is {determine_score_result(score)}')
    """ Determine result for random numbers """
    generate_score = random.randint(1, 100)
    print(f'The random score {generate_score} is {determine_score_result(generate_score)}')


def determine_score_result(score):
    if score > 100 or score < 0:
        return 'Invalid score'
    else:
        if score >= 90:
            return 'Excellent'
        elif score >= 50:
            return 'Pass'
        else:
            return 'Bad'


main()
