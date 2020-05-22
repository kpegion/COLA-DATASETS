import sys
import glob
import xarray as xr
import intake
import click
from framework import src_header
from framework import src_footer
@click.command()
@click.argument('path')
@click.argument('file_name')
@click.argument('dataset_name')
@click.argument('parent_page')

def generate_catalog(path, file_name, dataset_name, parent_page):
    """
    PATH:  The directory in COLAx server such as: '/shared/scratch/nbehboud/gridded/temp/' 

    FILE_NAME: If there are more than one file, FILE_NAME is the pattern for the NetCDF files, otherwise, Name of the NetCDF file. e.g.: 'air.mon.mean.nc' 

    DATASET_NAME: Name of the directory containing the NetCDf data files, e.g.: 'GHCN_CAMS'

    PARENT_PAGE: Name of the parent directory in the dataset type hierarchy, e.g.: Temperature
    """
    
    fileName = path+ dataset_name + "/"+ file_name
    nfiles = len(glob.glob(fileName))
    
    # Set is_combine based on number of files
    if (nfiles > 1):
        is_combine= True
        print("More than one file###")
    else:
        print("one file###")
        is_combine= False


    if int(is_combine) == True:
        # Read with xarray
        source = xr.open_mfdataset(fileName,combine='nested',concat_dim='time')
        src = source
        # Use intake with xarray kwargs
        source = intake.open_netcdf(fileName,concat_dim='time',xarray_kwargs={'combine':'nested','decode_times':True})
    else:
        source = intake.open_netcdf(fileName)
        src = xr.open_dataset(fileName)
        source.discover()

    dataset_name = open(dataset_name+'.yaml', 'w')
    dataset_name.write(source.yaml())
    dataset_name.close()
    print(str(dataset_name.name) + " was cataloged\n")
    
    #############################################

    # CATALOG_DIR: Github repository containing the master catalog
    # NOTE: It will be more accurate later
    catalog_dir = "https://github.com/kpegion/COLA-DATASETS-CATALOG"
    open_catalog = catalog_dir + "/"+ parent_page +".yaml"
    title = src.attrs['title'] 
    url = src.attrs['References'] 

    html_repr =xr.core.formatting_html.dataset_repr(src).replace('\\n', '\n')
    _header = src_header(title, parent_page,  open_catalog, url, catalog_dir)

    _footer = src_footer()
    html_src = _header + html_repr + _footer
    page_name = file_name.replace('*','').replace('..','.')

    html_page = page_name +".html" 
    with open(html_page , "w") as file:
        file.write(html_src)

    print( html_page + " was created\n")
if __name__ == "__main__":
    generate_catalog()

