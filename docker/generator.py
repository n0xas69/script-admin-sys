# Generate some containers with ssh for test environment

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("type", help="ubuntu, debian or centos")
parser.add_argument("number", help="number of containers to deploy", type=int)
args = parser.parse_args()

print(args.type)