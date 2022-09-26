'''
Score Menu
'''

MENU = '''
(G)et score
(D)isplay results
(P)rint stars
(Q)uit
'''


def main():
    score = 0
    print(MENU, end='')
    choice = str(input(">>> ")).upper()
    while choice != 'Q':
        if choice == "G":
            score = get_valid_score()
        elif choice == "D":
            print(f'Your score {score} is {determine_score_result(score)}', end='')
        elif choice == "P":
            print(f'You have {score} stars: ')
            print('*' * score, end='')
        else:
            print('Invalid choice!')
        print(MENU, end='')
        choice = str(input(">>> ")).upper()
    print("Thanks!")


def get_valid_score():
    """ Determine the valid score """
    score = int(input('Score: '))
    while score > 100 or score < 0:
        print('Invalid score')
        score = int(input('Score: '))
    return score


def determine_score_result(get_score):
    """ Will determine the result """
    if get_score >= 90:
        return 'Excellent'
    elif get_score >= 50:
        return 'Pass'
    else:
        return 'Bad'


main()
