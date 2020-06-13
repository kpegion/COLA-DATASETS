#!/bin/bash
DIR_daily=/shared/obs/gridded/CPC-PRECIP-CONUS/daily
DIR_monthly=/shared/obs/gridded/CPC-PRECIP-CONUS/monthly






cd $DIR_daily

for number in `seq 1948 2006`;do wget ftp://ftp2.psl.noaa.gov/Datasets/cpc_us_precip/precip.V1.0.$number.nc; done

cd $DIR_monthly

wget ftp://ftp.cdc.noaa.gov/Datasets/cpc_us_precip/precip.V1.0.mon.mean.nc

