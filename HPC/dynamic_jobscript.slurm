#!/bin/bash -l
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius
#SBATCH --cpus-per-task=4
#SBATCH --mem=10G
#SBATCH --time=02:00:00
#SBATCH -o ./logs/output_%j.out

TREE_FILES=("trees/btree.py" "trees/ternary_tree.py" "trees/ternary_tree_B.py" "trees/ternary_tree_minimalistic.py" "trees/ternary_tree_recursive.py")
FUNCTIONS=("dynamic_insert.py" "dynamic_search.py" "dynamic_search_exact.py")

for tree_file in "${TREE_FILES[@]}"; do
  for func in "${FUNCTIONS[@]}"; do
     /usr/bin/time -v python3 $func "$tree_file"  2>&1
  done
done


