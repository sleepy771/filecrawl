#!/usr/bin/env python3
from .elastic import Model


class FileIndexBuilder(Model):
    __idx__ = 'files'
    __doc_type__ = 'basic'

    def __init__(self, filepath):
        self._filepath = filepath
        self.mime_type = None
        self.meta_data = {}
        self.filename = None
        self.modification = None
        self.category = []
        self.tags = []

    @property
    def type(self):
        if self.mime_type is None:
            return None
        return self.mime_type.split('/')[0]

    @property
    def subtype(self):
        if self.mime_type is None:
            return None
        return self.mime_type.split('/')[1]

    def build(self):
        return {
            'file_path': self._filepath,
            'file_name': self.filename,
            'type': self.type,
            'subtype': self.subtype,
            'meta_data': self.meta_data,
            'tags': self.tags,
            'category': self.category,
            'modification': self.modification
        }

    def __str__(self):
        return str(self.build())