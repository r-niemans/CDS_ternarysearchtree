from datasets import load_dataset
import re

ds = load_dataset("StephanAkkerman/frequency-words-2018")
all_values = [row["text"] for row in ds["train"]]

regex_alpha = re.compile(r"[a-z]+")
filtered_values = [regex_alpha.findall(text) for text in all_values]

flat_values = [word for sublist in filtered_values for word in sublist]

output_filename = "frequency_words.txt"

# Write all words to a file, each on a new line
with open(output_filename, "w", encoding="utf-8") as f:
    for word in flat_values:
        f.write(word + "\n")  # Append '\n' to ensure each word is on a new line
