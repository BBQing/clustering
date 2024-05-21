import pytest
from jsonschema.exceptions import ValidationError


def test_kmeans(validator, valid_reader, valid_writer, valid_kmeans):
    entry = {
        "reader": valid_reader,
        "clustering": valid_kmeans,
        "writer": valid_writer,
    }

    assert validator(entry) is None

    entry["clustering"]["model_kwargs"] = {"n_clusters": 10}
    assert validator(entry) is None
    entry["clustering"]["model_kwargs"]["n_clusters"] = "invalid"
    with pytest.raises(ValidationError):
        validator(entry)
    entry["clustering"]["model_kwargs"]["n_clusters"] = 10
    entry["clustering"]["model_kwargs"]["nonexistent"] = 10
    with pytest.raises(ValidationError):
        validator(entry)
    del entry["clustering"]["model_kwargs"]["nonexistent"]
    entry["clustering"]["model_kwargs"]["bisecting_strategy"] = "largest_cluster"
    with pytest.raises(ValidationError):
        validator(entry)


def test_birch(validator, valid_reader, valid_writer, valid_birch):
    entry = {
        "reader": valid_reader,
        "clustering": valid_birch,
        "writer": valid_writer,
    }

    assert validator(entry) is None

    entry["clustering"]["model_kwargs"] = {"n_clusters": 10}
    assert validator(entry) is None
    entry["clustering"]["model_kwargs"]["n_clusters"] = "invalid"
    with pytest.raises(ValidationError):
        validator(entry)
    entry["clustering"]["model_kwargs"]["n_clusters"] = 10
    entry["clustering"]["model_kwargs"]["nonexistent"] = 10
    with pytest.raises(ValidationError):
        validator(entry)
    del entry["clustering"]["model_kwargs"]["nonexistent"]
    entry["clustering"]["model_kwargs"]["bisecting_strategy"] = "largest_cluster"
    with pytest.raises(ValidationError):
        validator(entry)
    del entry["clustering"]["model_kwargs"]["bisecting_strategy"]
    entry["clustering"]["model_kwargs"]["branching_factor"] = 5
    assert validator(entry) is None


def test_bisecting_kmeans(
    validator, valid_reader, valid_writer, valid_bisecting_kmeans
):
    entry = {
        "reader": valid_reader,
        "clustering": valid_bisecting_kmeans,
        "writer": valid_writer,
    }
    assert entry["clustering"]["model"] == "bisecting_kmeans"
    assert validator(entry) is None

    entry["clustering"]["model_kwargs"] = {"n_clusters": 10}
    assert validator(entry) is None
    entry["clustering"]["model_kwargs"]["n_clusters"] = "invalid"
    with pytest.raises(ValidationError):
        validator(entry)
    entry["clustering"]["model_kwargs"]["n_clusters"] = 10
    entry["clustering"]["model_kwargs"]["nonexistent"] = 10
    with pytest.raises(ValidationError):
        validator(entry)
    del entry["clustering"]["model_kwargs"]["nonexistent"]
    # entry["clustering"]["model_kwargs"]["bisecting_strategy"] = "largest_cluster"
    # assert validator(entry) is None
