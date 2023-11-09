import wandb

# Replace 'your_project' with your actual W&B project name
wandb.init(project='your_project', job_type="test_run")

# Log some arbitrary data
wandb.log({'test_metric': 42})

# Finish the W&B run
wandb.finish()

print("Done logging to W&B.")
