#!/bin/bash
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius
#SBATCH --job-name=btree
#SBATCH --output=logs/btree_%j.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=16G
#SBATCH --time=02:00:00

echo "running insert for btree.py"
srun --exclusive --cpu-bind=cores /usr/bin/time -v python3 ternary_tree/dynamic_insert.py ternary_tree/trees/btree.py 2>&1 | grep -E 'User time \(seconds\)|Elapsed.*time|Maximum resident set size'

echo "running search function for btree.py"
srun --exclusive --cpu-bind=cores /usr/bin/time -v python3 ternary_tree/dynamic_search.py ternary_tree/trees/btree.py 2>&1 | grep -E 'User time \(seconds\)|Elapsed.*time|Maximum resident set size'

echo "running search_exact for btree.py"
srun --exclusive --cpu-bind=cores /usr/bin/time -v python3 ternary_tree/dynamic_search_exact.py ternary_tree/trees/btree.py 2>&1 | grep -E 'User time \(seconds\)|Elapsed.*time|Maximum resident set size'

echo "btree.py has finished running"