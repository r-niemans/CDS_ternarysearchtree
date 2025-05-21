#!/usr/bin/env python

import importlib.util
import argparse
import random
import pickle

parser = argparse.ArgumentParser()
parser.add_argument("tree_path", type=str)
args = parser.parse_args()

spec = importlib.util.spec_from_file_location("tree_module", args.tree_path)
tree_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tree_module)

for name in dir(tree_module):
    obj = getattr(tree_module, name)
    if isinstance(obj, type) and 'insert' in dir(obj):
        tree = obj()
        break


with open("frequency_words.pkl", "rb") as f:
    flat_values = pickle.load(f)

insert_sample = random.sample(flat_values, k = 50000000)

for word in insert_sample:
    tree.insert(word)


