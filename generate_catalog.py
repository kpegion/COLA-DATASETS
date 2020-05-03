import sys
import xarray as xr
import intake

def generate_catalog(path, is_combine, file_name, dataset_name):

    if int(is_combine) == 1:
        print("here")
        f_combine_names= path+ dataset_name + "/"+ file_name
        # Read with xarray
        source = xr.open_mfdataset(f_combine_names,combine='nested',concat_dim='time')

        # Use intake with xarray kwargs
        source = intake.open_netcdf(f_combine_names,concat_dim='time',xarray_kwargs={'combine':'nested','decode_times':True})
    else:
        print("there")
        fileName = path+dataset_name+"/"+file_name
        source = intake.open_netcdf(fileName)
        print(fileName) 
    source.discover()
    dataset_name = open(dataset_name+'.yaml', 'w')
    dataset_name.write(source.yaml())
    dataset_name.close()
    print(str(dataset_name.name) + " was cataloged")
    

def main():
    if len(sys.argv) < 5:
        print("You have not provided enough info")
    else:
        generate_catalog(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])



if __name__ == "__main__": 
    main()

