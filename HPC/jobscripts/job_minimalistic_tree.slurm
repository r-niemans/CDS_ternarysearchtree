#!/bin/bash
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius
#SBATCH --job-name=ternary_tree_minimalistic
#SBATCH --output=logs/ternary_tree_minimalistic_%j.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00

echo "running insert for ternary_tree_minimalistic.py"
srun --exclusive --cpu-bind=cores /usr/bin/time -v python3 ternary_tree/dynamic_insert.py ternary_tree/trees/ternary_tree_minimalistic.py 2>&1 | grep -E 'User time \(seconds\)|Elapsed.*time|Maximum resident set size'

echo "running search function for ternary_tree_minimalistic.py"
srun --exclusive --cpu-bind=cores /usr/bin/time -v python3 ternary_tree/dynamic_search.py ternary_tree/trees/ternary_tree_minimalistic.py 2>&1 | grep -E 'User time \(seconds\)|Elapsed.*time|Maximum resident set size'

echo "running search_exact for ternary_tree_minimalistic.py"
srun --exclusive --cpu-bind=cores /usr/bin/time -v python3 ternary_tree/dynamic_search_exact.py ternary_tree/trees/ternary_tree_minimalistic.py 2>&1 | grep -E 'User time \(seconds\)|Elapsed.*time|Maximum resident set size'

echo "ternary_tree_minimalistic.py has finished running"