import argparse
from itertools import cycle, count, islice


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('my_list', nargs='+', type=int)
    parser.add_argument('stop', type=int)  # number or repetitions
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    print(list(islice(cycle(namespace.my_list), namespace.stop)))
