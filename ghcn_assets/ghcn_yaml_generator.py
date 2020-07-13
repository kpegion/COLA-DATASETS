import xarray as xr
import intake

path='/shared/scratch/nbehboud/gridded/temp/GHCN_CAMS/'
mean_temp = 'air.mon.mean.nc'

# Use intake with xarray kwargs
source = intake.open_netcdf(path+mean_temp)
source.discover()


mean_outf = open('ghcn_cams.yaml', 'w')
mean_outf.write(source.yaml())
mean_outf.close()

