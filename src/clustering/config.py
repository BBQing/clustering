import os

import yaml  # type: ignore
from jsonschema import Draft202012Validator, validate

schema = {
    "type": "object",
    "properties": {
        "reader": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "format": {
                    "type": "string",
                    "enum": ["json", "numpy"],
                },
            },
            "required": ["path", "format"],
        },
        "clustering": {
            "type": "object",
            "properties": {
                "model": {
                    "type": "string",
                    "enum": ["kmeans", "birch", "bisecting_kmeans"],
                },
                "model_kwargs": {
                    "allOf": [
                        {
                            "if": {"properties": {"model": {"const": "kmeans"}}},
                            "then": {"$ref": "#/$defs/kmeans_kwargs"},
                        },
                        {
                            "if": {"properties": {"model": {"const": "birch"}}},
                            "then": {"$ref": "#/$defs/birch_kwargs"},
                        },
                        {
                            "if": {
                                "properties": {"model": {"const": "bisecting_kmeans"}}
                            },
                            "then": {"$ref": "#/$defs/bisecting_kmeans_kwargs"},
                        },
                    ],
                },
            },
        },
        "writer": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "format": {"type": "string", "enum": ["json", "numpy"]},
            },
            "required": ["format", "path"],
        },
    },
    "required": ["reader", "clustering", "writer"],
    "$defs": {
        "kmeans_kwargs": {
            "type": "object",
            "properties": {
                "n_clusters": {"type": "integer"},
                "init": {"type": "string"},
                "n_init": {"type": "integer"},
                "max_iter": {"type": "integer"},
                "tol": {"type": "number"},
                "verbose": {"type": "integer"},
                "random_state": {"type": "integer"},
                "copy_x": {"type": "boolean"},
                "algortihm": {"type": "string", "enum": ["lloyd", "elkan"]},
            },
            "additionalProperties": False,
        },
        "birch_kwargs": {
            "type": "object",
            "properties": {
                "threshold": {"type": "number"},
                "branching_factor": {"type": "integer"},
                "n_clusters": {"type": "integer"},
                "compute_labels": {"type": "boolean"},
                "copy": {"type": "boolean"},
            },
            "additionalProperties": False,
        },
        "bisecting_kmeans_kwargs": {
            "type": "object",
            "properties": {
                "n_clusters": {"type": "integer"},
                "init": {"type": "string", "enum": ["kmeans++", "random"]},
                "n_init": {"type": "integer"},
                "random_state": {"type": "integer"},
                "max_iter": {"type": "integer"},
                "verbose": {"type": "integer"},
                "tol": {"type": "number"},
                "copy_x": {"type": "boolean"},
                "algortihm": {"type": "string", "enum": ["lloyd", "elkan"]},
                "bisecting_strategy": {
                    "type": "string",
                    "enum": ["biggest_inertia", "largest_cluster"],
                },
            },
            "additionalProperties": False,
        },
    },
}


def parse_config(path: str) -> dict:
    with open(path, "r") as f:
        raw_config = yaml.safe_load(f)

    validate(raw_config, schema=schema, cls=Draft202012Validator)

    return raw_config
