#!/usr/bin/env python3
from filecrawl.typeguess import guess_mimetype, is_archive


def test_type_guess():
    filenames = [
        'foo.ogg',
        'bar.csv',
        'baz.xml',
        'qux.json',
        'quux.epub'
    ]
    mime_types = [
        'application/octet-stream',
        'text/csv',
        'application/xml',
        'application/json',
        'application/epub+zip'
    ]
    assert mime_types == [guess_mimetype(fn) for fn in filenames]


def test_multitypes():
    filenames = [
        'foo.tar.gz',
        'bar.tar.bz2',
        'baz.gz',
        'qux.info.json'
    ]
    mime_types = [
        'application/tar+gzip',
        'application/tar+bzip2',
        'application/gzip',
        'application/json'
    ]
    assert mime_types == [guess_mimetype(fn) for fn in filenames]


def test_is_archive():
    mimetypes = [
        'application/tar',
        'application/tar+gzip',
        'application/tar+bzip2',
        'application/gzip',
        'application/json',
        'application/octet-stream',
        'application/zip',
        'text/plain'
    ]
    expected = [
        True,
        True,
        True,
        True,
        False,
        False,
        True,
        False
    ]
    assert expected == [is_archive(m) for m in mimetypes]