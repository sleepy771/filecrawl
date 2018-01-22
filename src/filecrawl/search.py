#!/usr/bin/env python3
from elasticsearch import Elasticsearch

ES = Elasticsearch(hosts=['localhost'])

if __name__ == '__main__':
    # search = {
    #     'query': {
    #         'nested': {
    #             'path': 'meta_data',
    #             'query': {
    #                 'match': {
    #                     'meta_data.title': 'guide'
    #                 }
    #             }
    #         }
    #     }
    # }
    search = {
        'query': {
            'bool': {
                'must': [
                    {
                        'match': {
                            'file_name': 'crad'
                        }
                    },
                    # {'term': {'subtype': 'csv'}}
                ]
            }
        }
    }

    document = ES.search(index='files', doc_type='basic', body=search)['hits']['hits']
    for doc in document:
        meta_data = doc['_source']['meta_data']
        file_path = doc['_source']['file_path']
        print(meta_data.get('authors', meta_data.get('author', None)), meta_data.get('title', None))
        print(meta_data)
        print(doc['_source'])
        print(file_path)
