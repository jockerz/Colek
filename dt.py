#!/usr/bin/python3
import argparse
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument('timestamp', type=int, help="timestamp (integer)")
parser.add_argument('-u', '--utc', help="convert to UTC",
                    action='store_true', default=False)


def main(timestamp, utc=False):
    if utc:
        return datetime.utcfromtimestamp(timestamp)
    else:
        return datetime.fromtimestamp(timestamp)


if __name__ == '__main__':
    args = parser.parse_args()
    print(main(args.timestamp, True if args.utc else False))
