import json

import numpy


class Writer:

    def __init__(self, path: str, encoding: str = "utf-8"):
        self.path = path
        self.encoding = encoding

    def write(self, data):
        raise NotImplementedError()


class JSONWriter(Writer):

    def write(self, data):
        with open(self.path, "w", encoding=self.encoding) as file:
            json.dump(data, file)


class NumpyWriter(Writer):

    def write(self, data):
        numpy.save(self.path, data)
