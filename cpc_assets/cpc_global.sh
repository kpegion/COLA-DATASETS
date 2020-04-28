#!/bin/bash
DIR=/scratch/nbehboud/gridded/temp/CPC-GLOBAL





cd $DIR
# README file
wget ftp://ftp.cdc.noaa.gov/Datasets/cpc_global_temp/README
for number in `seq 1979 2020`; do wget ftp://ftp.cdc.noaa.gov/Datasets/cpc_global_temp/tmax.$number.nc; done


for number in `seq 1979 2020`; do wget ftp://ftp.cdc.noaa.gov/Datasets/cpc_global_temp/tmin.$number.nc; done

