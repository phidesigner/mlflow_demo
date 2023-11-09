import argparse


def out_demo(text):
    print(f"out_demo: {text}")
    return text


def main(args):
    out_demo(args.text)


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
