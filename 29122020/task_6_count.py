import argparse
from itertools import count, islice


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('start', type=int)
    parser.add_argument('stop', type=int)
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    print(list(islice(count(namespace.start), namespace.stop)))