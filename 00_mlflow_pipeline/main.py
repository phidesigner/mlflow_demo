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

    if __name__ == "__main__":
        main()
