#/usr/bin/env python

import argparse

# yet to add time and memory comparison in this file

arg_parser= argparse.ArgumentParser(description='Load dataset and implement Ternary Tree')
arg_parser.add_argument('dataset', type=str, help='Path to dataset')
arg_parser.add_argument('ternary_tree', type=str, help='Tree structure')
args = arg_parser.parse_args()

print(f'Dataset: {args.dataset}')
print(f'Ternary Tree Type: {args.ternary_tree}')

