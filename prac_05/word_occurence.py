"""
Word Occurrence
Estimate: 120 minutes
Actual: 130 minutes
"""


def main():
    word_to_count = {}

    get_text = input('Text: ')
    words = get_text.split()
    count_occurrence(word_to_count, words)

    words = list(word_to_count.keys())
    words.sort()

    max_length = max(len(word) for word in words)
    for word in words:
        print(f'{word:{max_length}} : {word_to_count[word]}')


def count_occurrence(word_to_count, words):
    for word in words:
        occurrence = word_to_count.get(word, 0)
        word_to_count[word] = occurrence + 1


main()
