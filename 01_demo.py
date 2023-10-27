from mlflow import log_metric, log_param, log_artifact
from random import choice

def main():
    metrics = ['foo', 'bar', 'baz']

    percentages = [i for i in range(100)]

    for i in range(40):
        log_metric(choice(metrics), choice(percentages))

# mlflow experiments create --experiment-name "My Experiment"
# $env:MLFLOW_EXPERIMENT_ID = "153514638190734289"; mlflow run .


if __name__ == '__main__':
    main()