#!/usr/bin/env python3
from elasticsearch import Elasticsearch
from .config import ELASTIC_HOSTS


ES_CLIENT = None


class Model:
    __idx__ = None
    __doc_type__ = None

    def build(self):
        return self.__dict__

    def save(self):
        client = get_es_client()
        client.index(
            self.__class__.__idx__,
            self.__class__.__doc_type__,
            self.build()
        )


def get_es_client():
    """Returns lazy instantiated Elastic search client object.

    Returns:
        Elasticsearch: Elasticsearch object.
    """
    global ES_CLIENT
    if ES_CLIENT is None:
        ES_CLIENT = Elasticsearch(hosts=ELASTIC_HOSTS)
    return ES_CLIENT


def put_mappings():
    import json
    from pathlib import Path
    client = get_es_client()
    mappings = get_mappings()
    for mapping in mappings:
        mp = Path(mapping)
        name = mp.name[-len(mp.suffix):]
        index, doc_type = name.split('_', maxsplit=1)
        with open(mapping, 'rb') as mapping_fd:
            mapping_data = json.loads(str(mapping_fd.read(), encoding='utf-8'))
            client.indices.create(index)
            client.indices.put_mapping(doc_type, mapping_data, index=index)


def get_mappings():
    from os.path import join, dirname, normpath
    import os
    dir_path = normpath(join(dirname(__file__), '../../mappings/'))
    mappings = join(dir_path, [f for f in os.listdir(dir_path) if f.endswith('.json')])
    return mappings
