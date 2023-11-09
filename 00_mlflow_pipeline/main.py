import os
import hydra
from omegaconf import DictConfig
import mlflow


@hydra.main(config_name="config")
def main(cfg: DictConfig):
    os.environ["WANDB_PROJECT"] = cfg["main"]["project_name"]
    os.environ["WANDB_RUN_GROUP"] = cfg["main"]["experiment_name"]

    root_path = hydra.utils.get_original_cwd()

    _ = mlflow.run(
        os.path.join(root_path, 'in'),
        "main",
        parameters={
            'text': cfg['input']['text']
        }
    )
    _ = mlflow.run(
        os.path.join(root_path, 'out'),
        'main',
        parameters={
            'text': cfg['output']['text']
        }
    )


if __name__ == "__main__":
    main()
