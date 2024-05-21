import json

import numpy


class Reader:

    def __init__(self, path: str, encoding: str = "utf-8"):
        self.path = path
        self.encoding = encoding

    def read(self):
        raise NotImplementedError()


class JSONReader(Reader):

    def read(self):
        with open(self.path, encoding=self.encoding) as file:
            return json.load(file)


class NumpyReader(Reader):

    def read(self):
        return numpy.load(self.path)
