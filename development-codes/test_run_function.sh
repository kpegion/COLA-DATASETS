#!/bin/bash -x


function foo() {
  python3.6 /homes/nbehboud/COLA-DATASETS-CATALOG/development-codes/generate_catalog.py $1 $2 $3
  #python /homes/kpegion/pythondev/COLA-DATASETS-CATALOG/development-codes/generate_catalog.py $1 $2 $3
  if [ $? -eq 0 ]
	then
	  echo "$2 Success"
	else
	  echo "$2 Failed !!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	fi
}



filename='data_backup.txt'


while IFS=$'\t' read -r -a line ; do
theFile=${line[0]}
theDataset=${line[1]}
theTags=${line[2]}


intake_catalogs="/homes/kpegion/pythondev/COLA-DATASETS-CATALOG/intake-catalogs"
html_files="/homes/kpegion/pythondev/COLA-DATASETS-CATALOG"

yaml_file=*.yaml
html_file=*.html

#temp_dir=${line[1]}
#mkdir ${temp_dir}_temporary
#pushd ${temp_dir}_temporary



foo $theFile $theDataset	$theTags
#mv $yaml_file $intake_catalogs
#mv $html_file $html_files
#echo "---------------------------------------------------------------------------------------"
##popd
done < $filename

