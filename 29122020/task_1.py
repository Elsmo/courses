import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('time', type=int)
    parser.add_argument('per_hour', type=int)
    parser.add_argument('award', type=int)
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    print(f'Salary: {namespace.time * namespace.per_hour + namespace.award}')


