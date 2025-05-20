#!/bin/bash -l
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:15:00

start1=$(date +%s)
python insert_test.py
end1=$(date +%s)
echo "insert_time.py execution time: $((end1-start1)) seconds"

start2=$(date +%s)
python search_exact_test.py
end2=$(date +%s)
echo "search_exact_test.py execution time: $((end2-start2)) seconds"

start3=$(date +%s)
python search_test.py
end3=$(date +%s)
echo "search_test.py execution time: $((end3-start3)) seconds"

