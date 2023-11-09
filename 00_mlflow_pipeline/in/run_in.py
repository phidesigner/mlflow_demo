import argparse


def in_demo(text):
    print(f"in_demo: {text}")
    return text


def main(args):
    in_demo(args.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='in_demo')

    parser.add_argument(
        '--text',
        type=str,
        default='default text in',
        help='The message to print'
    )

    args = parser.parse_args()
    main(args)