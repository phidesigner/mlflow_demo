import argparse


def out_demo(text):
    print(f"out_demo: {text}")
    return text


def main(args):
    # out_demo(args.text)

    wandb.init(job_type="output_processing")

    # Load input artifact
    artifact = wandb.use_artifact('processed_text_artifact:latest')
    artifact_path = artifact.file()

    # Load data
    with open(artifact_path, 'r') as f:
        data = json.load(f)
    processed_text = data['processed_text']

    out_demo(processed_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='out_demo')

    parser.add_argument(
        '--text',
        type=str,
        default='default text out',
        help='The message to print'
    )

    args = parser.parse_args()
    main(args)
