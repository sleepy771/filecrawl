#!/usr/bin/env python3
from filecrawl.extractors import is_invalid_date


def test_is_invalid_date():
    dates = [
        '2016 February',
        'abcdef',
        '1516610815.776386',
        '1.516610815776386e9',
        '2016-12-05 10:22:11.0001',
        '2016',
        '2016-02',
        '2016-2-1',
        '2016-1-1 12'
    ]
    expected = [
        True,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False
    ]
    assert expected == [is_invalid_date(d) for d in dates]
