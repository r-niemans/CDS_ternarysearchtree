from datasets import load_dataset

ds = load_dataset("kossnocorp/wikipedia-words-en-low")

all_values = [row["word"] for row in ds["train"]]
# all_values = sorted(all_values)    # sorted version
output_filename = "wikipedia.txt"   # wikipedia2.txt for the sorted version

# Write all words to a file, each on a new line
with open(output_filename, "w", encoding="utf-8") as f:
    for word in all_values:
        f.write(word + "\n")  # Append '\n' to ensure each word is on a new line
