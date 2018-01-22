#!/usr/bin/env python3

ELASTIC_HOSTS = []


_ALLOWED_TYPES = [str, int, float, list, type(None), dict]


def _init_config():
    import os
    _substitute_globals(os.environ)


def _substitute_globals(dct):
    _g_vars = _read_config_variables()
    for k, v in dct.items():
        if k in _g_vars:
            hook = _set_hooks(k)
            globals()[k] = hook(v)


def _set_hooks(k):
    if k == 'ELASTIC_HOSTS':
        return lambda x: x.strip().split(',')
    else:
        return lambda x: x


def _read_config_variables():
    return [var for var, val in globals().items()
            if all([var.upper() == var,
                    not var.startswith('_'),
                    type(val) in _ALLOWED_TYPES])]


def _assert_config():
    assert ELASTIC_HOSTS, "Environment variable `ELASTIC_HOSTS` is not set"
