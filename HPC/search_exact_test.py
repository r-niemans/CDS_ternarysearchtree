from trees.ternary_tree_minimalistic import TernarySearchTreeSparse
import random 

with open("frequency_words.txt") as file:
    words = [line.strip() for line in file]
insert_sample = random.sample(words, k=1000000)

tst = TernarySearchTreeSparse()
for word in insert_sample:
    tst.insert(word)

insert_sample = random.sample(words, k=1000000)

for word in insert_sample:
    tst.search(word, exact=True)
