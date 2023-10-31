import os
import hydra
from omegaconf import DictConfig

@hydra.main(config_path="config", config_name="config")
def func(cfg: DictConfig):
    working_dir = os.getcwd()
    print(f"The current working directory is {working_dir}")
    
    orig_cwd = hydra.utils.get_original_cwd()

    # Read file
    path = f"{orig_cwd}/text.txt"
    with open(path, "r") as f:
        print(f.read())

    # Write file
    path = f"output.txt"
    with open(path, "w") as f:
        f.write("This is a new file created by the hydra_demo/01_hydra.py script")


if __name__ == "__main__":
    func()