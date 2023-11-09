import hydra
from omegaconf import DictConfig
import mlflow
import wandb


@hydra.main(config_name="config")
def main(cfg: DictConfig):
    _ = mlflow.run(
        path='/workspaces/mlflow_demo/00_mlflow_pipeline/in/run_in.py',
        name='main',
        parameters={
            'text': cfg['main']['text']
        }
    )

    _ = mlflow.run(
        path='/workspaces/mlflow_demo/00_mlflow_pipeline/out/run_out.py',
        name='main',
        parameters={
            'text': cfg['output']['text']
        }
    )

    if __name__ == "__main__":
        main()
