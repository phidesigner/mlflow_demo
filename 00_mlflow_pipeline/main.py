import hydra
from omegaconf import DictConfig
import mlflow
import wandb

@hydra.main(config_name="config")
def main(cfg: DictConfig):
    