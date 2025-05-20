from trees.ternary_tree_minimalistic import TernarySearchTreeSparse
import random
import pickle

with open("frequency_words.pkl", "rb") as f:
    flat_values = pickle.load(f)

insert_sample = random.sample(flat_values, k = 1000000)

tst = TernarySearchTreeSparse()
for word in insert_sample:
    tst.insert(word)