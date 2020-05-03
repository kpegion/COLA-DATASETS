import xarray as xr
import intake

path='/shared/scratch/nbehboud/gridded/temp/CPC-GLOBAL/'
f_max_names=path+'tmax.*.nc'
f_min_names=path+'tmin.*.nc'
print(f_max_names)
# Read with xarray
ds_max=xr.open_mfdataset(f_max_names,combine='nested',concat_dim='time')

# Use intake with xarray kwargs
source_max=intake.open_netcdf(f_max_names,concat_dim='time',xarray_kwargs={'combine':'nested','decode_times':True})
source_max.discover()


max_outf = open('cpc-global-tmax.yaml', 'w')
max_outf.write(source_max.yaml())
max_outf.close()




# Read with xarray
ds_min=xr.open_mfdataset(f_min_names,combine='nested',concat_dim='time')

# Use intake with xarray kwargs
source_min=intake.open_netcdf(f_min_names,concat_dim='time',xarray_kwargs={'combine':'nested','decode_times':True})
source_min.discover()


min_outf = open('cpc-global-tmin.yaml', 'w')
min_outf.write(source_min.yaml())
min_outf.close()



