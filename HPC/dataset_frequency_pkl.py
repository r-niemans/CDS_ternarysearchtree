from datasets import load_dataset
import re
import pickle

ds = load_dataset("StephanAkkerman/frequency-words-2018")
all_values = [row["text"] for row in ds["train"]]

regex_alpha = re.compile(r"[a-z]+")
filtered_values = [regex_alpha.findall(text) for text in all_values]

flat_values = [word for sublist in filtered_values for word in sublist]

with open("frequency_words.pkl", "wb") as f:
    pickle.dump(flat_values, f)


