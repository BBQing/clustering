import pytest

from clustering.containers import Container

# {
#     "reader": {"format": "json", "path": "data.json"},
#     "clustering": {
#         "model": "kmeans",
#     },
#     "writer": {"format": "numpy", "path": "output.npy"},
# }


@pytest.fixture(scope="module")
def container():
    _container = Container()
    _container.wire()
    yield _container
    _container.unwire()
