from functools import partial

import pytest
from jsonschema import Draft202012Validator, validate

from clustering.config import schema
from clustering.containers import Container


@pytest.fixture
def container():
    _container = Container()
    _container.wire()
    yield _container
    _container.unwire()


@pytest.fixture
def validator():
    return partial(validate, cls=Draft202012Validator, schema=schema)


@pytest.fixture
def valid_reader():
    return {"format": "json", "path": "input.json"}


@pytest.fixture
def valid_writer():
    return {"format": "json", "path": "output.json"}


@pytest.fixture
def valid_kmeans():
    return {"model": "kmeans"}


@pytest.fixture
def valid_birch():
    return {"model": "birch"}


@pytest.fixture
def valid_bisecting_kmeans():
    return {"model": "bisecting_kmeans"}
