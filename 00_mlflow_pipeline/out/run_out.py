import argparse
import wandb
import json


def out_demo(text, add_text):
    print(f"out_demo: {text} + {add_text} ")
    return text + " " + add_text


def main(args):
    # out_demo(args.text)

    wandb.init(
        project='workflow_demo',
        name='run_out'
    )

    # Load input artifact
    artifact = wandb.use_artifact(
        "artifact_demo_file:latest",
        type='demo')

    artifact_path = artifact.file()

    # Load data
    with open(artifact_path, 'r') as f:
        data = json.load(f)
    original_text = data['processed_text']

    # Modify the text using additional text from args
    modified_text = out_demo(original_text, args.add_text)

    # Log the modified text as a new artifact
    modified_artifact = wandb.Artifact(
        'artifact_demo_file',
        type='demo'     # Same type as the input artifact
    )
    with modified_artifact.new_file("text_demo.json", mode="w") as f:
        json.dump({'processed_text': modified_text}, f)

    wandb.log_artifact(modified_artifact)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='out_demo')

    parser.add_argument(
        '--add_text',
        type=str,
        required=True,
        help='Additional text to modify the original text'
    )

    args = parser.parse_args()
    main(args)
