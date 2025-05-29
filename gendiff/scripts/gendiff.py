import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Generate differences between two files."
    )
    parser.add_argument('first_file', help=argparse.SUPPRESS)
    parser.add_argument('second_file', help=argparse.SUPPRESS)
    parser.add_argument(
        "-h", "--help", action="help", help="show this help massage and exit"
    )
    args = parser.parse_args()
    print('Gendiff is ready to rock! Use -h for help')


if __name__ == '__main__':
    main()
