#!/bin/bash


function foo() {
  python3.6 /homes/nbehboud/COLA-DATASETS-CATALOG/generate_catalog.py $1 $2 $3 $4
  if [ $? -eq 0 ]
	then
	  echo "$2 Success"
	else
	  echo "$2 Failed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	fi
}



filename='data.txt'


while IFS=$'\t' read -r -a line ; do
theFile=${line[0]}
theDataset=${line[1]}
theParent=${line[2]}
theTags=${line[3]}


temp_dir=${line[2]}
mkdir temporary_$temp_dir
cd temporary_$temp_dir

foo $theFile $theDataset $theParent $theTags
done < $filename

