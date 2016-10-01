import sys
import operator
import re

from collections import Counter


def load_data(filepath):
    with open(filepath) as data_file:
        return data_file.read()


def get_words(text):
    return re.findall(r'[а-яёЁА-ЯA-z\']+', text.lower())


def get_most_frequent_words(text, count_words=10):
    words = get_words(text)
    return Counter(words).most_common(count_words)


def show_dict(dict_obj):
    for key, value in dict_obj:
        print(u'%s %s' % (key, value))


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("File don`t enter. Please run script with argv.")
        sys.exit()
    most_frequent_words = get_most_frequent_words(load_data(sys.argv[1]))
    show_dict(most_frequent_words)
