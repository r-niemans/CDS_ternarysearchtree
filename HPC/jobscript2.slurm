#!/bin/bash -l
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius
#SBATCH --cpus-per-task=4
#SBATCH --mem=10G
#SBATCH --time=02:00:00
#SBATCH -o ./logs/output_%j.out

start1=$(date +%s)
/usr/bin/time -v python insert_test2.py 2>&1
end1=$(date +%s)
echo "insert_time2.py execution time: $((end1-start1)) seconds"

start2=$(date +%s)
/usr/bin/time -v python search_exact_test2.py 2>&1
end2=$(date +%s)
echo "search_exact_test2.py execution time: $((end2-start2)) seconds"

start3=$(date +%s)
/usr/bin/time -v python search_test2.py 2>&1
end3=$(date +%s)
echo "search_test2.py execution time: $((end3-start3)) seconds"

