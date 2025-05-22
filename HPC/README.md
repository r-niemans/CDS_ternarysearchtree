## HPC Folder

This folder contains the various Python scripts and Slurm scripts used for benchmarking the ternary search tree and binary tree.

The evaluation was first conducted using `jobscript.slurm`, which automates the timing of three key functions: insert, search, and search exact. Each insert, search and search_exact python scripts allow tuning the number of words to be tested for each function. Each SLURM execution was repeated three times per tree type, ensuring consistent measurements across all trees.
Tests were performed on two datasets:
- `frequency_words`, which contains a large number of words.
- `wikipedia`, which consists of more distinct and elaborated words.
Additionally, performance comparisons were made between around 2M words from the `frequency_words`, `wikipedia`'s unsorted dataset and a sorted list of Wikipedia words, specifically to analyze the impact of tree balance on execution times.

In a further step and to improve efficiency, we optimized the .slurm file (`dynamic_jobscript.slurm`) by incorporating slightly more advanced Bash functions, allowing us to test all tree operations—including insert, prefix search, and exact search—within a single file while monitoring the maximum resident set size for every function execution per tree. After successfully doing this within one single file, we also ran a .slurm file per tree to discover whether optimized performance was reached, but that did not contribute much to an improved to nor to a more moderate memory usage. 
Additionally, we switched from using text files (created from the large datasets) to pickle files. Pickle files help save and load data much faster which makes our programs run more efficiently than before.
The results were then compared with the initial tests to assess performance improvements.
