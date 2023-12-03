import argparse
import wandb
import json


def in_demo(text):
    print(f"in_demo: {text}")
    return text


def main(args):

    wandb.init(
        project="workflow_demo",
        name='run_in')

    processed_text = in_demo(args.text)

    artifact = wandb.Artifact(
        name='artifact_in_demo',
        type='in_demo'
    )

    with artifact.new_file('text_demo.json', mode='w') as f:
        json.dump({'processed_text': processed_text}, f)

    wandb.log_artifact(artifact)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='in_demo')

    parser.add_argument(
        '--text',
        type=str,
        default='### Default from in_demo.py ###',
        help='The message to print'
    )

    args = parser.parse_args()
    main(args)
