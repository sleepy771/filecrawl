#!/usr/bin/env python3
from pathlib import Path
from .extractors import (
    epub_metadata_extractor,
    dummy_mime_info_extractor,
    pdf_metadata_extractor
)
from os.path import (
    getmtime,
    getatime,
    getsize
)


_ASSOCIATED_TYPES = {
    ('.rst',): 'text/x-rst',
    ('.py',): 'text/x-py',
    ('.c',): 'text/x-c',
    ('.cpp',): 'text/x-c',
    ('.pdf',): 'application/pdf',
    ('.epub',): 'application/epub+zip',
    ('.mobi',): 'application/x-mobipocket-ebook ',
    ('.txt',): 'text/plain',
    ('.json',): 'application/json',
    ('.js',): 'application/js',
    ('.tar', '.gz'): 'application/tar+gzip',
    ('.tgz',): 'application/tar+gzip',
    ('.tar',): 'application/tar',
    ('.html',): 'text/html',
    ('.htm',): 'text/html',
    ('.css',): 'text/css',
    ('.xml',): 'application/xml',
    ('.jpeg',): 'image/jpeg',
    ('.jpg',): 'image/jpeg',
    ('.png',): 'image/png',
    ('.webm',): 'video/webm',
    ('.avi',): 'video/avi',
    ('.yaml',): 'application/x-yaml',
    ('.csv',): 'text/csv',
    ('.zip',): 'application/zip',
    ('.log',): 'text/x-log',
    ('.gz',): 'application/gzip',
    ('.bz2',): 'application/bzip2',
    ('.tar', '.bz2'): 'application/tar+bzip2'
}


def guess_mimetype(filename):
    path = Path(filename)
    suffixes = tuple(path.suffixes)
    k = 0
    while suffixes[k:] not in _ASSOCIATED_TYPES and k < len(suffixes) - 1:
        k += 1
    return _ASSOCIATED_TYPES.get(suffixes[k:], 'application/octet-stream')


_MIME_EXTRACTORS = {
    'application/epub+zip': epub_metadata_extractor,
    'application/pdf': pdf_metadata_extractor,
    'application/x-mobipocket-ebook': None,
    'image/jpeg': None,
    'image/png': None,
    'video/avi': None,
    'video/webm': None
}


def get_mime_extractor(mimetype):
    return _MIME_EXTRACTORS.get(mimetype, dummy_mime_info_extractor)


_TEXT_EXTRACTORS = {
    'text/plain': None,
    'text/html': None,
}


_CATEGORY = {
    'application/epub+zip': ['Book'],
    'application/x-mobipocket-ebook': ['Book'],
    'application/pdf': ['Book', 'Paper', 'Document'],
    'text/x-rst': ['Document'],
    'text/x-c': ['Source'],
    'text/x-py': ['Source'],
    'text/csv': ['Table', 'Data', 'Structured'],
    'text/plain': ['Text', 'Document'],
    'application/json': ['Tree', 'Data', 'Structured'],
    'application/xml': ['Tree', 'Data', 'Structured'],
    'application/x-yaml': ['Tree', 'Data', 'Structured'],
    'text/x-log': ['Logfile', 'Time series', 'Events'],
    'application/gzip': ['Archive'],
    'application/bzip2': ['Archive'],
    'application/tar+gzip': ['Archive'],
    'application/tar+bzip2': ['Archive'],
    'application/tar': ['Archive'],
    'application/zip': ['Archive']
}


def guess_category(mimetype):
    return _CATEGORY.get(mimetype, [])


def get_file_metainfo(filepath):
    return {
        'size': getsize(filepath),
        'access_time': getatime(filepath),
        'modify_time': getmtime(filepath)
    }


def is_archive(mimetype):
    return 'Archive' in guess_category(mimetype)