import sys
import operator
import re


def load_data(filepath):
    with open(filepath) as data_file:
        return data_file.read()


def get_dict(text):
    data = re.findall(r'[а-яёЁА-ЯA-z\']+', text)
    word_dict = {}
    for word in data:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict


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
