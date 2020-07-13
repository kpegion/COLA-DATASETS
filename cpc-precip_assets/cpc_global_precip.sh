#!/bin/bash
DIR=/shared/obs/gridded/CPC-PRECIP


cd $DIR
# README file
wget ftp://ftp.cdc.noaa.gov/Datasets/cpc_global_precip/README
for number in `seq 1979 2020`; do wget ftp://ftp.cdc.noaa.gov/Datasets/cpc_global_precip/precip.$number.nc; done


