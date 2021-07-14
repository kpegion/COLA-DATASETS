#!/bin/bash

target="/homes/nbehboud/COLA-DATASETS-CATALOG/development-codes/data_backup.txt"
for filename in d_data_backup/va850/daily/full/*/*.txt; do
	mv  $filename $target
	vim $target -c ':wq'
	bash run_function.sh
	echo "$filename processed"
done


