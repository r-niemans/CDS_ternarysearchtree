# Concepts of Data Science 2024-2025 - Implementation of a Ternary Search Tree

## Project Description :
The project aims at implementing a ternary search tree using Python.
The goal is to explore different ternary search trees and explore their efficiencies in handling searches and insertions. The goal is also to test their performance with small and large dataset on high performance computing (HPC) infrastuctures. 
The following flowchart illustrates our strategy.
```mermaid
flowchart LR
    Start(["🔹 Start"])-- Rafke/Sophie -->Find_Datasets
    Start(["🔹 Start"])-- Rafke/Sophie -->Create_TSTs
    Start(["🔹 Start"])--Sophie-->Optimize_Binary_Tree

    subgraph Dataset_Selection
        Find_Datasets -- Rafke --> Big_Datasets
        Find_Datasets -- Sophie --> Small_Datasets
        Big_Datasets --> id1["Wikipedia Words (2.6M)"]
        Big_Datasets --> id2["Frequency Words (50M)"]
        Small_Datasets --> id3["Corncob Lowercase (50k)"]
        Small_Datasets --> id4["Words Alpha (300k)"]
    end
    style Dataset_Selection fill:#FFDDC1,stroke:#FF5722

    subgraph Tree_Construction
        Create_TSTs--Rafke/Sophie -->Ternary_Tree
        Create_TSTs--Sophie-->Ternary_Tree_Iterative
        Create_TSTs--Rafke-->Ternary_Tree_Sparse
        Create_TSTs--Rafke-->Ternary_Tree_HighlyRecursive
        Optimize_Binary_Tree--Sophie-->Binary_Tree
    end
    style Tree_Construction fill:#C1E1FF,stroke:#2196F3

    subgraph Performance_Testing
        Binary_Tree --Rafke--> Unit_tests
        Ternary_Tree --Rafke--> Unit_tests
        Ternary_Tree_Iterative --Rafke--> Unit_tests
        Ternary_Tree_Sparse --Rafke--> Unit_tests
        Ternary_Tree_HighlyRecursive --Rafke--> Unit_tests
        Unit_tests --> Performance_tests_small
        Performance_tests_small --Sophie--> id5["Small Dataset Sizes [10,100,1000,10k,50k, 300k]"]
        id5 --> Performance_tests_big
        Performance_tests_big --Rafke--> id6["Big Dataset Sizes [500k,1M,2M,5M,10M,20M,50M]"]
        Performance_tests_big --Sophie--> id6["Big Dataset Sizes [500k,1M,2M,5M,10M,20M,50M]"]
    end
    style Performance_Testing fill:#D1FFD1,stroke:#388E3C

    subgraph Documentation_Feedback
        Unit_tests --Rafke/Sophie --> Documentation
        id5 --Rafke/Sophie --> Documentation
        id6 --Rafke/Sophie --> Documentation
    end
    style Documentation_Feedback fill:#FFD1D1,stroke:#D32F2F
    Documentation --> End(["🛑 End"])
```
We started by developing our first ternary search tree (TST) `ternary_tree.py` using an object-oriented approach in Python, based on the binary tree from the course materials. To meet the requirements for prefix searches and exact searches, we made slight modifications to the binary tree structure in  `btree.py`. \
After that, we divided our work into creating three or more different TSTs, each with unique performance characteristics: an iterative version `ternary_tree_B.py`, a sparse version `ternary_tree_minimalistic.py`, and a highly recursive version `ternary_tree_recursive.py`. \
Alongside the implementation, we searched for various datasets—including small samples like the `corncob_lowercase.txt` dataset from the course, the `words_alpha.txt` [^1] dataset, as well as larger datasets exceeding one million words. We took two large datasets (one from `wikipedia` words [^2], and the other from `frequency_words` in 2018[^3]). It was assumed that the variety and complexity of words in the wikipedia dataset is larger than the frequency words where this is more a quantitative dataset that could lead to some differences in the inserting and searching times. \
To ensure correctness, we performed unit tests for our different trees, making sure they passed a set of edge cases we designed in the `test_tst.py`. Once all trees were properly refactored and functional, we conducted performance tests using datasets of various sizes. These tests measured the insert and search speed of each TST under different conditions. The binary tree was also evaluated together with those TST.
For smaller dataset benchmarks, we performed the test locally, where the results are available in the Jupyter Notebook in `tst_implementations.ipynb`. We used the `corncob_lowercase` and `words` dataset. \
For large dataset benchmarks, we used HPC infrastructure with Vlaamse Supercomputing Centrum [^4]. \
The output results and the scripts are available in the `HPC` folder and Discussion and conclusion on our results are available in the following sections.

## Contents
### Repository structure 
And below is a more comprised diagram, showing the working of the repository. 

```mermaid
flowchart TD
    %% Data Stores
    subgraph "Data Stores"
        DSLocal["Local Datasets<br/>(small)"]:::data
        ExternalDS["External Datasets<br/>(large)"]:::data
    end

    %% Core Library
    TL["Tree Library<br/>(TST & BTree Variants)"]:::core

    %% Local Environment
    subgraph "Local Workstation"
        UT["Unit Test Harness"]:::test
        TR["Test Results"]:::test
        LB["Local Benchmark Notebook"]:::test
        LM["Local Metrics"]:::test
    end

    %% HPC Environment
    subgraph "HPC Cluster"
        HC["HPC Client Scripts"]:::test
        SL["SLURM Scheduler"]:::service
        CN["Compute Nodes"]:::env
        OS["HPC Output Storage"]:::data
    end

    %% Workflow Arrows
    DSLocal -->|"ingest (insert/search)"| TL
    ExternalDS -->|"ingest (insert/search)"| HC

    TL -->|"run tests"| UT
    UT -->|"generate results"| TR

    TL -->|"benchmark with small data"| LB
    LB -->|"collect metrics"| LM

    HC -->|"submit jobs"| SL
    SL -->|"execute on"| CN
    CN -->|"store logs & metrics"| OS

    %% Interconnections
    TL --> HC

    %% Click Events
    click DSLocal "https://github.com/r-niemans/cds_ternarysearchtree/tree/main/data/"
    click DSLocal "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/data/corncob_lowercase.txt"
    click DSLocal "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/data/insert_words.txt"
    click DSLocal "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/data/not_insert_words.txt"
    click DSLocal "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/data/words_alpha.txt"
    click DSLocal "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/data/README.md"
    click ExternalDS "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/dataset_frequency.py"
    click ExternalDS "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/dataset_frequency_pkl.py"
    click ExternalDS "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/dataset_wiki_pkl.py"
    click TL "https://github.com/r-niemans/cds_ternarysearchtree/tree/main/trees/"
    click TL "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/trees/btree.py"
    click TL "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/trees/ternary_tree.py"
    click TL "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/trees/ternary_tree_B.py"
    click TL "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/trees/ternary_tree_minimalistic.py"
    click TL "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/trees/ternary_tree_recursive.py"
    click UT "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/test_tst.py"
    click LB "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/tst_implementations.ipynb"
    click HC "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/insert_test.py"
    click HC "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/insert_test2.py"
    click HC "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/search_test.py"
    click HC "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/search_test2.py"
    click HC "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/search_exact_test.py"
    click HC "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/search_exact_test2.py"
    click HC "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/tst_full_execution.py"
    click HC "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/vsc_py_file.py"
    click SL "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/jobscript.slurm"
    click SL "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/jobscript2.slurm"
    click OS "https://github.com/r-niemans/cds_ternarysearchtree/blob/main/HPC/Outputs/slurm-out.zip"

    %% Styles
    classDef core fill:#D6EAF8,stroke:#1B4F72,color:#1B2631;
    classDef test fill:#D5F5E3,stroke:#196F3D,color:#0B5345;
    classDef data fill:#FCF3CF,stroke:#B7950B,color:#7D6608,shape:cylinder;
    classDef env fill:#FADBD8,stroke:#C0392B,color:#641E16;
    classDef service fill:#E8DAEF,stroke:#7D3C98,color:#4A235A,shape:roundrect;
```


## Performance Testing : Small Datasets
In smaller datasets, **recursive trees** show relatively stable insertion times but with some fluctuations, indicating possible efficiency changes at different scales. That can be explained by the overhead of recursive function calls, becoming more noticeable depending on data distribution and tree depth. **Iterative trees** have inconsistent performance, with near-zero values at some sample sizes but increasing times at larger sizes. **Sparse trees** maintain generally lower and more predictable times, suggesting moderate efficiency in handling structured data. **B-trees** excel at small sample sizes, showing zero times for up to 1,000 entries, before gradually increasing at **10,000 and beyond**, reinforcing their ability to manage small-scale datasets efficiently. That reflects the B-trees strength of a balanced structure and node-level storage, which minimizes insertion operations for small datasets.  

Overall, **B-trees are the best choice for small data**, while **iterative trees show unpredictability**, and **recursive and sparse trees demonstrate moderate but stable performance** based on the data provided. 

## Performance Testing : Large Datasets using HPC infrastructure

### Datasets as.txt files
Based on the result data generated in the HPC (available in the Output folder), we observed that B-trees consistently show the fastest insertion and searching times, making them the most efficient overall, while recursion-based TST struggles at larger sample sizes, even failing at 50M entries (recursion depth exceeded error). Iterative trees offer stable performance, maintaining reasonable insertion and search times without extreme jumps, whereas sparse trees show increasing complexity as sample sizes grow. Exact searching times remain low for smaller sample sizes but increase significantly for larger datasets. The presence of errors in recursion and some inconsistencies in sparse tree performance suggest scalability challenges, whereas B-trees remain consistently efficient even as data size grows. This analysis highlights the importance of selecting the right tree structure based on dataset size and operational requirements.

### Datasets as .pkl files
Besides loading the data from a .txt file, executions were done with extracting data from pickle files as well. These are generally faster than raw text files because they store data in a binary format that can be loaded directly into memory as structured Python objects, thus avoiding string processing required with text files. Pickle is especially efficient for large lists. In some cases, such as when dealing with very large pickled objects, memory usage during deserialization can be high. In contrast, raw text files are slower to process but are more portable and easier to debug or stream in chunks, due to simplicity. 

### Comparison of the trees with Different Datasets having ~2M words)
Performance comparisons were made between around 2M words from the `frequency_words`, `wikipedia`'s unsorted dataset and a sorted list of Wikipedia words (`wikipedia_sorted`) specifically to analyze the impact of tree balance on execution times. 
Results from the output in the HPC folder were pooled and summary graphs were created and are available in the [Outputs](https://github.com/r-niemans/CDS_ternarysearchtree/tree/main/HPC/Outputs) folder. 

As observed, pickle files generally show faster insertion and searching times compared to text files for datasets containing around 2 million words. 
* Recursion B-trees consistently show the best performance, with the lowest insertion and searching times, except for `wikipedia_sorted`, where searching was not possible due to a recursion error. 
* Recursion-based TST trees perform poorly, especially with sorted datasets, as their searching times increase significantly and can even cause errors. 
Iterative trees maintain stable performance with reasonable insertion and searching times, making them a balanced alternative. 
* Sparse trees show growing complexity as dataset sizes increase, leading to higher insertion and searching times, making them less scalable. 
* The `frequency_words` dataset has a more limited word spread, resulting in lower searching times, while Wikipedia has a higher variety of words, leading to longer searching times. On the contrary, `wikipedia_sorted`, being a sorted version of Wikipedia, has the highest searching times, showing that sorting negatively affects recursive structures. 

It can be concluded that for a specific size, choosing the right tree structure depends on dataset type and spread, with B-trees being the most efficient except in highly sorted cases.


## Performance Testing : Comparison with B-Trees
Comparing a TST to a Binary Search Tree (B-tree), the memory trade-off is subtle: a B-tree stores a full string once, whereas a TST spreads each string across nodes but shares prefixes. This is especially visible when comparing the performances of TSTs and B-trees on the small datasets, where a B-tree performs noticeably well and fast. If ordered traversal or prefixed lookup is required, a TST performs better and the TST-based method is known to achieve shorter runtime and higher accuracy. 

## Discussion : Time and Space Complexity
When the input list is sorted or semi-sorted, a ternary search tree (TST) can become unbalanced, degrading its insertion time complexity from O(log n) to O(n), thus making it linear link of nodes rather than a logarithmic link, while its space complexity remains O(n). This happens because each character comparison may consistently follow only left or right branches, never balancing across all three, which causes the TST to behave like a linked list. \
As a result, longer paths are created, and more edges must be traversed, leading to higher insertion times. In recursive TST implementations, this imbalance is worsened by deep recursion, which can trigger a RecursionError, as seen in `ternary_tree.py` and `ternary_tree_recursive.py`. \
Consequently, the shorter the path, the better the hierarchical relationships are captured. Additionally, to allow models to learn these long-term patterns, the historical input to the models should also be long and in that case a low time and space complexity becomes even more relevant [^5]. 
Next, `ternary_tree_B.py` and `ternary_tree_minimalistic.py` exhibit excessive memory usage (up to ~10 GB) due to either added metadata or lack of object overhead prevention, leading to large numbers of unshared nodes and deeper nesting. 
Moreover, `ternary_tree_minimalistic.py` includes no optimization properties resulting in every insert spawning new nodes. \
In contrast, `btree.py` remains efficient (~5.3 GB) due to its compact structure, shallow depth, iterative insertion, and storage of multiple keys per node, which significantly reduces the number of node allocations. In a TST, n refers to the number of strings, with each insert potentially creating one node per character, while in a BST, n typically represents full words. \
The sparse structure of unoptimized TSTs means more pointers and strings are stored per word; therefore, it is more efficient to prefix or compress shared paths. If words are long and share prefixes, TSTs are more space-efficient. Ultimately, poor tree balance leads not only to degraded performance but also to increased memory consumption, especially when large and sorted datasets are involved.

## Conclusion
We tested different tree structures to understand their performance in various situations. Using **unit tests and HPC benchmarks**, we analyzed how trees handle insertion and searching for small and large datasets. \
We attempted to classify our trees in a quadrant chart based on speed and scale.
We conclude that **binary trees** work best overall, with fast insertion and search times. **Recursive trees** struggle as datasets grow, especially with sorted data, where they become inefficient or even fail. **Iterative trees** perform steadily but show unpredictable behavior in small datasets. **Sparse trees** maintain reasonable efficiency at small scales but become slower as dataset sizes increase. 
Our results highlight how **dataset size and structure**, and **the types of the tree** affect tree performance, showing the importance of choosing the right tree based on efficiency and scalability.
When looking at documentation we could further study by looking at Tries which seem to be more interesting for prefix searches, or self-balancing binary search trees such as the AVL (Adelson-Velsky and Landis) trees or red-black trees to tackle the issue of unbalanced trees [^6]. Moreover, B+ trees could be another alternative to look at, especially when working with range queries. They store data pointers at the leaf nodes of the tree and not at internal nodes, like the regular B-tree. We were also thinking about ameliorating our benchmarking processes by putting our trees in pickle files.

## References:

[^1]: [DWYL English Words](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) – A dataset containing a comprehensive list of English words.  
[^2]: [Hugging Face Wikipedia Words](https://huggingface.co/datasets/kossnocorp/wikipedia-words-en-low) – A dataset of English words extracted from Wikipedia for NLP tasks.  
[^3]: [Frequency Words 2018](https://huggingface.co/datasets/StephanAkkerman/frequency-words-2018) – A dataset of frequently used English words based on 2018 language data.  
[^4]: [KU Leuven HPC On-Demand](http://ondemand.hpc.kuleuven.be/) – A platform for accessing high-performance computing resources at KU Leuven.
[^5]: Liu, S., Yu, H., Liao, C., Li, J., Lin, W., Liu, A. X., & Dustdar, S. (2022). Pyraformer: Low-Complexity Pyramidal Attention for Long-Range Time Series Modeling and Forecasting. In Proceedings of the Tenth International Conference on Learning Representations (ICLR 2022). https://doi.org/10.34726/2945
[^6]: Schwarz, K. (2015). Lecture 15: Tries and Suffix Trees. CS166: Advanced Data Structures. Stanford University. Retrieved from https://web.stanford.edu/class/archive/cs/cs166/cs166.1256/lectures/15/Lecture%20Slides.pdf
