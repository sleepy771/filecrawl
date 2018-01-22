#!/usr/bin/env python3
from os import walk
from os.path import join, getmtime

from filecrawl.typeguess import (
    guess_mimetype,
    get_mime_extractor,
    guess_category
)
from filecrawl.utils import (
    filename_to_nametags
)
from filecrawl.es_models import FileIndexBuilder


def crawl(superpath):
    for superpath, dirs, files in walk(superpath):
        for file in files:
            full_path = join(superpath, file)
            fi = FileIndexBuilder(full_path)

            fi.mime_type = guess_mimetype(full_path)
            extractor = get_mime_extractor(fi.mime_type)
            fi.filename = ' '.join(filename_to_nametags(full_path))
            if extractor:
                fi.meta_data = extractor(full_path)
            fi.modification = getmtime(full_path)
            fi.category = guess_category(fi.mime_type)
            fi.save()


if __name__ == '__main__':
    crawl('/home/filip/Dokumenty')