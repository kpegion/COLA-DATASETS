#!/bin/bash
DIR_w=/shared/obs/gridded/OISSTv2/weekly
DIR_m=/shared/obs/gridded/OISSTv2/monthly
DIR_mask=/shared/obs/gridded/OISSTv2/lmask



cd $DIR_w
wget ftp://ftp.cdc.noaa.gov/Datasets/noaa.oisst.v2/sst.wkmean.1981-1989.nc
wget ftp://ftp.cdc.noaa.gov/Datasets/noaa.oisst.v2/sst.wkmean.1990-present.nc


cd $DIR_m
wget ftp://ftp.cdc.noaa.gov/Datasets/noaa.oisst.v2/sst.mnmean.nc


cd $DIR_mask
wget ftp://ftp.cdc.noaa.gov/Datasets/noaa.oisst.v2/lsmask.nc

