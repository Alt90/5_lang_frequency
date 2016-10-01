import sys
import operator
import re

from collections import Counter


def load_data(filepath):
    with open(filepath) as data_file:
        return data_file.read()


def get_text_lower_words(text):
    return text.lower()


def get_list_words(text):
    return re.findall(r'[а-яёЁА-ЯA-z\']+', get_text_lower_words(text))


def get_dict(text):
    word_dict = Counter()
    for word in get_list_words(text):
        word_dict[word] += 1
    return dict(word_dict)


def sort_dict(text_dict):
    return sorted(text_dict.items(), key=operator.itemgetter(1), reverse=True)


def get_most_frequent_words(text_dict, count_words=10):
    for key, value in sort_dict(text_dict)[:count_words]:
        print(u'%s %s' % (key, value))


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("File don`t enter. Please run script with argv.")
        sys.exit()
    text = load_data(sys.argv[1])
    text_dict = get_dict(text)
    get_most_frequent_words(text_dict)
