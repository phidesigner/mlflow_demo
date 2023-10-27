"""
This module logs random metrics using mlflow.
"""

from random import choice
from mlflow import log_metric


def main():
    """
    Logs random metrics using mlflow.
    """
    metrics = ['foo', 'bar', 'baz']
    percentages = list(range(100))

    for i in range(100):
        log_metric(choice(metrics), choice(percentages))


if __name__ == '__main__':
    main()
