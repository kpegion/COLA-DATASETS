#!/bin/bash

for f in *\ *; do mv "$f" "${f// /_}"; done
target="html_paths.txt"
#target="/homes/nbehboud/COLA-DATASETS-CATALOG/development-codes/html_paths.txt"
for filename in d_html_paths/*; do
	mv  $filename $target
	#vim $target -c ':wq'
	bash test_run_fake.sh
	echo "$filename processed"
done


