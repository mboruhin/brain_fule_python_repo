from urllib.request import urlopen
from typing import List
import sys


def get_text(url):
    """gets text from URL"""
    story = urlopen(url)
    word_list = []
    for line in story:
        # print(str(line))
        line_words = line.split()
        for word in line_words:
            word_list.append(word)
    story.close()
    return word_list


def print_text(words: List[str]):
    """ blablablablablabla"""
    for word in words:
        print(word)

def test():
    main(r'https://sixty-north.com/c/t.txt')


def main(url:str):
    print_text(get_text(url))


aaa = "aaaaaaaaaaaaaa"

def randon_func_crap(string: str = aaa):
    print(string)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('usage: python get_words_from_site <url>')
    main(sys.argv[1])
    # print('Argument List:', str(sys.argv))
    # print('Argument List:', sys.argv[0])
    # print(type(sys.argv[0]))
    # print(sys.argv)