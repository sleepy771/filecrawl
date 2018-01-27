#!/usr/bin/env python3
import re

from epub_meta import get_epub_metadata
from PyPDF2 import PdfFileReader
from hachoir.core.tools import makeUnicode
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from hachoir.metadata.metadata import Metadata


DATE_TIME_REGEX = re.compile(
    r'^\s*([-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?'
    r'|'
    r'\d+(-\d{1,2}){0,2}(\s+\d{1,2}(:\d{1,2}){0,2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?)?)\s*$'
)


def dummy_text_extractor(filepath):
    return ''


def plain_extractor(filepath):
    with open(filepath, 'r') as f:
        return ' '.join(f.readlines())


def dummy_mime_info_extractor(filepath):
    return {}


def epub_metadata_extractor(filepath):
    meta_data = dict(get_epub_metadata(filepath, read_cover_image=False, read_toc=False))
    if is_invalid_date(meta_data['publication_date']):
        meta_data['publication_date'] = None
    return meta_data


def hachoir_metadata_extractor(filepath):
    parser = createParser(filepath)

    if not parser:
        raise Exception('Parser not found')

    with parser:
        try:
            metadata = extractMetadata(parser)
        except Exception as err:
            print('Some error occured: %s', err)
            metadata = None

        meta_dct = extract_hachoir_metatdata_dictionary(metadata)
        print(meta_dct)


def extract_hachoir_metatdata_dictionary(metadata, title=None):
    if not metadata:
        return {}
    if not title:
        title = metadata.header
    data = {title: {}}
    for d in metadata:
        if not d.values:
            continue
        data[title][d.key] = []
        for item in d.values:
            data[title][d.key] = makeUnicode(item.value)
    return data



def is_invalid_date(datetime_str):
    return DATE_TIME_REGEX.match(datetime_str) is None


def mobi_metadata_extractor(filepath):
    pass


def pdf_metadata_extractor(filepath):
    with open(filepath, 'rb') as pdf_file:
        reader = PdfFileReader(pdf_file)
        pdf_info = reader.getDocumentInfo()
        metadata = {
            'authors': pdf_info.author,
            'title': pdf_info.title,
            'creator': pdf_info.creator,
            'producer': pdf_info.producer,
            'subject': pdf_info.subject
        }
        return metadata


if __name__ == '__main__':
    hachoir_metadata_extractor('/home/filip/Stiahnuté/big_buck_bunny_1080p_stereo.ogg')