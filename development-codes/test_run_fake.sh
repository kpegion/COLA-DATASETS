#!/bin/bash


function foo() {
  python3.6 /homes/nbehboud/COLA-DATASETS-CATALOG/development-codes/fake_generate.py $1
  if [ $? -eq 0 ]
	then
	  echo "$1 Success"
	else
	  echo "$1 Failed !!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	fi
}



filename='html_paths.txt'


while IFS=$'\t' read -r -a line ; do
theFile=${line[0]}


intake_catalogs="/homes/nbehboud/COLA-DATASETS-CATALOG/intake-catalogs"
#html_files="/homes/nbehboud/COLA-DATASETS-CATALOG"

yaml_file=*.yaml
#html_file=*.html


foo $theFile
#mv $yaml_file $intake_catalogs
#mv $html_file $html_files
echo "---------------------------------------------------------------------------------------"
#popd
done < $filename

