import argparse
import wandb


def in_demo(text):
    print(f"in_demo: {text}")
    return text


def main(args):
    print("Initializing W&B...")
    wandb.init(job_type="input")
    print("W&B initialized.")

    processed_text = in_demo(args.text)
    print(f"Logging processed text to W&B: {processed_text}")
    wandb.log({"processed_text": processed_text})
    print("Logged to W&B.")

    artifact = wandb.Artifact(
        'processed_text_artifact',  # Name of the artifact
        type='processed_text',      # Type of the artifact
        description='Processed text data'
    )
    with artifact.new_file("processed_text.json", mode="w") as f:
        json.dump({'processed_text': processed_text}, f)

    wandb.log_artifact(artifact)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='in_demo')

    parser.add_argument(
        '--text',
        type=str,
        default='default text in',
        help='The message to print'
    )

    args = parser.parse_args()
    print(f"Received text: {args.text}")
    main(args)
