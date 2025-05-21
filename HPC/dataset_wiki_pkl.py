from datasets import load_dataset
import pickle

ds = load_dataset("kossnocorp/wikipedia-words-en-low")

all_values = [row["word"] for row in ds["train"]]
# all_values = sorted(all_values)    # sorted version

with open("wikipedia.pkl", "wb") as f:
    pickle.dump(all_values, f)