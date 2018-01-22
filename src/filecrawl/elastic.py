#!/usr/bin/env python3
from elasticsearch import Elasticsearch


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
        ES_CLIENT = Elasticsearch(hosts=['localhost'])
    return ES_CLIENT


def put_mappings():
    import json
    import os.path
    client = get_es_client()
    with open(os.path.join(os.path.dirname(__file__), '../../types/mapping.json'), 'rb') as mapping_file:
        mapping = json.loads(str(mapping_file.read(), encoding='utf-8'))
        client.indices.create('files')
        client.indices.put_mapping('basic', mapping, index='files')
