#!/bin/bash
DIR_monthly=/shared/obs/gridded/CMAP/monthly
DIR_pentad=/shared/obs/gridded/CMAP/pentad


cd $DIR_monthly

wget ftp://ftp.cdc.noaa.gov/Datasets/cmap/std/precip.mon.mean.nc


cd $DIR_pentad
wget ftp://ftp.cdc.noaa.gov/Datasets/cmap/std/precip.pentad.mean.nc

