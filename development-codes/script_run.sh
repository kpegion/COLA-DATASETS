#!/bin/bash

target="/homes/nbehboud/COLA-DATASETS-CATALOG/development-codes/data_backup.txt"
for filename in ddddd/*.txt; do
	mv  $filename $target
	vim $target -c ':wq'
	bash run_function.sh
	echo "$filename processed"
done


