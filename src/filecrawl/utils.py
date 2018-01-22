#!/usr/bin/env python3
import re
import pathlib
from unidecode import unidecode

WORDS_REGEX = re.compile('(?:([a-zA-Z0-9]+)[^a-zA-Z0-9]*)')


def filename_to_nametags(filepath):
    return split_to_words(unidecode(strip_to_name(filepath)))


def strip_to_name(filepath):
    pth = pathlib.Path(filepath)
    suffix = ''.join(pth.suffixes)
    return pth.name[:-len(suffix)]


def split_to_words(filename):
    return [w.lower() for w in WORDS_REGEX.findall(filename)]


if __name__ == '__main__':
    print(strip_to_name('/home/filip/Dokumenty/walter_rudin__Principles_of_mathematical_analysis.pdf'))
    print(split_to_words('walter-rudin__Principles_of_mathematical_analysis.pdf'))