#!/bin/bash


function foo() {
  python3.6 /homes/nbehboud/COLA-DATASETS-CATALOG/development-codes/generate_catalog.py $1 $2 $3
  if [ $? -eq 0 ]
	then
	  echo "$2 Success"
	else
	  echo "$2 Failed !!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	fi
}



filename='data_backup.txt'

intake_catalogs="/homes/nbehboud/COLA-DATASETS-CATALOG/intake-catalogs"
html_files="/homes/nbehboud/COLA-DATASETS-CATALOG"

yaml_file=*.yaml
html_file=*.html

while IFS=$'\t' read -r -a line ; do
theFile=${line[0]}
theDataset=${line[1]}
theTags=${line[2]}



#temp_dir=${line[1]}
#mkdir ${temp_dir}_temporary
#pushd ${temp_dir}_temporary



foo $theFile $theDataset	$theTags
#mv $yaml_file $intake_catalogs
#mv $html_file $html_files
echo "---------------------------------------------------------------------------------------"
#popd
done < $filename

if ls *.yaml
	then mv $yaml_file $intake_catalogs
fi
if ls *.html 
then mv $html_file $html_files
fi
