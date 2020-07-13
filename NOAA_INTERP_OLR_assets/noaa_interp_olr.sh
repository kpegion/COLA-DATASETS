#!/bin/bash
DIR=/shared/obs/gridded/NOAA_INTERP_OLR




cd $DIR
# README file
wget ftp://ftp.cdc.noaa.gov/Datasets/olrcdr/olr.day.mean.nc
wget ftp://ftp.cdc.noaa.gov/Datasets/olrcdr/olr.mon.mean.nc


