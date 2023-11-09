"""
This module demonstrates how to use MLflow to log parameters, metrics, and artifacts.
"""

import mlflow
from mlflow import log_metric, log_param, log_artifact


def main():
    """
    This function logs parameters, metrics, and artifacts using MLflow.
    """
    # Log a parameter (key-value pair)
    log_param("param1", 5)

    # Log a metric; metrics can be updated throughout the run
    log_metric("foo", 1)
    log_metric("foo", 3)
    log_metric("foo", 6)

    # Log an artifact (output file)
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("Hello world!")
    log_artifact("output.txt")


if __name__ == '__main__':
    main()
