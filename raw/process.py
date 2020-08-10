import argparse
import json
import sys


def main(index: int, sort: str, filename: str):
    with open(filename, 'r') as f:
        items = [sort + ':' + json.loads(l)['id'] for l in f]
    for a, b in enumerate(range(0, len(items), 150000)):
        with open('{}_{}.txt'.format(str(a+index).zfill(2), sort), 'w') as f:
            f.write('\n'.join(items[b:b+150000]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--index', required=True, type=int)
    parser.add_argument('--type', required=True, type=str)
    parser.add_argument('--filepath', required=True, type=str)
    args = parser.parse_args()
    main(args.index, args.type, args.filepath)

