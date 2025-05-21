# Concept of Data Science 2024-2025 - Implementation of a Tenary Search Tree

## Project Description :
The project aims at implementing a ternary search tree using Python.
The goal is to explore different ternary search trees and explore their efficiencies in handling searches and insertions. The goal is also to test their performance with small and large dataset on an HPC infrastuctures. 
The following flowchart illustrates our strategy.
```mermaid
flowchart TD
    Start-- Rafke/Sophie -->Create_TSTs
    Create_TSTs--Rafke/Sophie -->Ternary_Tree_A
    Create_TSTs--Sophie-->Ternary_Tree_B
    Create_TSTs--Rafke-->Ternary_Tree_C
    Create_TSTs--Rafke-->Ternary_Tree_D
    Binary_Tree --> Unit_tests
    Ternary_Tree_A --> Unit_tests
    Ternary_Tree_B --> Unit_tests
    Ternary_Tree_C --> Unit_tests
    Ternary_Tree_D --> Unit_tests
    Unit_tests --> Performance_tests_small
    Performance_tests_small --> id5["Datasets sizes[10,100,1000,10000,500000,100000,300000]"]
    id5 --> Performance_tests_big
    Performance_tests_big --> id6["Datasets sizes[500000,1M,2M,5M,10M,20M,50M]"]
    Start-- Rafke/Sophie -->Modify_Binary_Tree --> Binary_Tree
    Start-- Rafke/Sophie -->Find_Datasets
    Find_Datasets -- Rafke --> Big_Datasets
    Find_Datasets -- Sophie --> Small_Datasets
    Big_Datasets --> id1["wikipedia-words-en-low (2.6 M words)"]
    Big_Datasets --> id2["frequency-words-2018 (50 M words)"]
    Small_Datasets --> id3["(corncob_lowercase.txt (50k words))"]
    Small_Datasets --> id4["(words_alpha.txt  (300k words))"]
    Unit_tests --> Documentation
    id5 --> Documentation
    id6 --> Documentation
    Documentation --> End
```

## Repository structure 
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

## Contents and how to run the Project
We started by developing our first ternary search tree (TST) `ternary_tree.py` using an object-oriented approach in Python, based on the binary tree from the course materials. To meet the requirements for prefix searches and exact searches, we made slight modifications to the binary tree structure in  `btree.py`. \
After that, we divided our work into creating three or more different TSTs, each with unique performance characteristics: an iterative version `ternary_tree_B.py`, a sparse version `ternary_tree_minimalistic.py`, and a highly recursive version `ternary_tree_recursive.py`. \
Alongside the implementation, we searched for various datasets—including small samples like the `corncob_lowercase.txt` dataset from the course, the `words_alpha.txt` [^1] dataset, as well as larger datasets exceeding one million words. We took two large datasets (one from `wikipedia` words [^2], and the other from `frequency_words` in 2018[^3]). It was assumed that the variety and complexity of words in the wikipedia dataset is larger than the frequency words where this is more a quantitative dataset that could lead to some differences in the inserting and searching times. \
To ensure correctness, we performed unit tests for our different trees, making sure they passed a set of edge cases we designed in the `test_tst.py`. Once all trees were properly refactored and functional, we conducted performance tests using datasets of various sizes. These tests measured the insert and search speed of each TST under different conditions. The binary tree was also evaluated together with those TST.
For smaller dataset benchmarks, we performed the test locally, where the results are available in the Jupyter Notebook in `tst_implementations.ipynb`. We used the `corncob_lowercase` and `words` dataset. \
For large dataset benchmarks, we used High Performance Computing (HPC) infrastructure with Vlaamse Supercomputing Centrum [^4]. \
The output results and the scripts are available in the `HPC` folder.

## Performance Testing : Small Datasets

## Performance Testing : Large Datasets using HPC infrastructure

## Performance Testing : Comparison with B-Trees

## Discussion : Time and Space Complexity

## Conclusion


## References:

[^1]: [DWYL English Words](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) – A dataset containing a comprehensive list of English words.  
[^2]: [Hugging Face Wikipedia Words](https://huggingface.co/datasets/kossnocorp/wikipedia-words-en-low) – A dataset of English words extracted from Wikipedia for NLP tasks.  
[^3]: [Frequency Words 2018](https://huggingface.co/datasets/StephanAkkerman/frequency-words-2018) – A dataset of frequently used English words based on 2018 language data.  
[^4]: [KU Leuven HPC On-Demand](http://ondemand.hpc.kuleuven.be/) – A platform for accessing high-performance computing resources at KU Leuven.
