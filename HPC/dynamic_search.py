#!/usr/bin/env python
import importlib.util
import argparse
import random
import pickle
import inspect

parser = argparse.ArgumentParser()
parser.add_argument("tree_path", type=str)
args = parser.parse_args()

spec = importlib.util.spec_from_file_location("tree_module", args.tree_path)
tree_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tree_module)

tree = None
for name, obj in inspect.getmembers(tree_module, inspect.isclass):
    if hasattr(obj, 'insert'):  # You can extend to also check for search, etc.
        tree = obj()
        break

if tree is None:
    raise Exception("No tree class found.")

with open("frequency_words.pkl", "rb") as f:
    flat_values = pickle.load(f)

insert_sample = random.sample(flat_values, k = 50_000_000)

for word in insert_sample:
    tree.search(word, exact=False)


