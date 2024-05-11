import os

import yaml  # type: ignore


def parse_config(path: str) -> dict:
    with open(path, "r") as f:
        raw_config = yaml.safe_load(f)

    validate_reader(raw_config)
    validate_clustering(raw_config)
    validate_writer(raw_config)

    return raw_config


def validate_reader(raw_config: dict):
    if "reader" not in raw_config:
        raw_config["reader"] = dict()
    if raw_config["reader"] is None:
        raise ValueError("Invalid 'reader' type - reader cannot be Nonetype")
    reader = raw_config["reader"]

    if "path" not in reader:
        reader["path"] = "data.json"
    if "format" not in reader:
        reader["format"] = "json"
    elif reader["format"] not in ["json", "numpy"]:
        raise ValueError("Invalid reader format")


def validate_writer(raw_config: dict):
    if "writer" not in raw_config:
        raw_config["writer"] = dict()
    if raw_config["writer"] is None:
        raise ValueError("Invalid 'writer' type - writer cannot be Nonetype")
    writer = raw_config["writer"]

    if "path" not in writer:
        writer["path"] = "output"
    if "format" not in writer:
        writer["format"] = "numpy"
    elif writer["format"] not in ["json", "numpy"]:
        raise ValueError("Invalid writer format")


def validate_clustering(raw_config: dict):
    if "clustering" not in raw_config:
        raise ValueError("Provide 'clustering' section")
    if raw_config["clustering"] is None:
        raise ValueError(
            "'clustering' section is empty - provide non-empty key 'model'"
        )
    clustering = raw_config["clustering"]

    if "model" not in clustering:
        raise ValueError(
            "Provide 'model' with value in ['kmeans', 'birch', 'bisecting_kmeans']"
        )
    if clustering["model"] not in ["kmeans", "birch", "bisecting_kmeans"]:
        raise ValueError(
            "Provide 'model' with value in ['kmeans', 'birch', 'bisecting_kmeans']"
        )
    if "model_kwargs" not in clustering:
        clustering["model_kwargs"] = dict()
    if clustering["model_kwargs"] is None:
        clustering["model_kwargs"] = dict()
