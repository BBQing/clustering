import pytest

from clustering.containers import Container


@pytest.fixture(scope="module")
def container():
    _container = Container()
    _container.wire()
    yield _container
    _container.unwire()
