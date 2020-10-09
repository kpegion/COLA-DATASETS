import sys
import glob
import xarray as xr
import intake
import click
from fake_framework import src_header
from update import update_json, update_parents, catalog_parent, update_links
import os, re
import subprocess as S
import pdb
@click.command()
@click.argument('file_path')



def fake_generate_catalog(file_path):
    
    path_array = file_path.split('/')
    path_array.remove('')

    try:
        arr.remove('shared')
    except:
        pass

    
    try:
        arr.remove('data')
    except:
        pass

    
    path_array = list(map(lambda x:x.lower(),path_array))

    current = ""
    parent = ""
    ancestors = ""
    
    for i in range(len(path_array)-1, 0 , -1):
        current = path_array[i]
        parent = path_array[i-1]
        ancestors = path_array[1:i-1]
    
        dp_name = parent+".html"
        if not os.path.isfile(dp_name):
            make_html(path_array[i-1], path_array[i-2], path_array[1:i-2])
            
        update_links(current, parent)




def make_html(current, parent, ancestors):
    
    catalog_dir = "https://raw.githubusercontent.com/kpegion/COLA-DATASETS-CATALOG/gh-pages/intake-catalogs/"
    open_catalog = catalog_dir + current +".yaml"
    title = current

    _header = src_header(title, ancestors,  open_catalog)

    html_page = current +".html"

    with open(html_page , "w", encoding='utf-8') as file:
        file.write(_header)
        print( html_page + " was created\n")

    os.rename(html_page, "../"+html_page)



if __name__ == "__main__":
    fake_generate_catalog()


