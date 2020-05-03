import sys
import xarray as xr
import intake
import click

@click.command()
@click.argument('path')
@click.argument('is_combine')
@click.argument('file_name')
@click.argument('dataset_name')

def generate_catalog(path, is_combine, file_name, dataset_name):
    """
    PATH:  The directory in COLAx server such as: '/shared/scratch/nbehboud/gridded/temp/' 

    IS_COMBINE: If there are more than one NetCDF datafiles which should be comined (1 or 0)

    FILE_NAME: If IS_COBINE is 1, FILE_NAME is the pattern for the NetCDF files, otherwise, Name of the NetCDF file. e.g.: 'air.mon.mean.nc' 

    DATASET_NAME: Name of the directory containing the NetCDf data files, e.g.: 'GHCN_CAMS'

    """
    
    if int(is_combine) == 1:
        f_combine_names= path+ dataset_name + "/"+ file_name
        # Read with xarray
        source = xr.open_mfdataset(f_combine_names,combine='nested',concat_dim='time')

        # Use intake with xarray kwargs
        source = intake.open_netcdf(f_combine_names,concat_dim='time',xarray_kwargs={'combine':'nested','decode_times':True})
    else:
        fileName = path+dataset_name+"/"+file_name
        source = intake.open_netcdf(fileName)
    source.discover()
    dataset_name = open(dataset_name+'.yaml', 'w')
    dataset_name.write(source.yaml())
    dataset_name.close()
    print(str(dataset_name.name) + " was cataloged")
    


if __name__ == "__main__":
    generate_catalog()

