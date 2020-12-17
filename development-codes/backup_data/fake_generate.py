import sys
from os.path import abspath
import glob
import click
from fake_framework import src_header
from update import update_json, make_ancestors, catalog_parent, link_to_children
import os, re
import subprocess as S
import pdb
@click.command()
@click.argument('file_path')



def fake_generate_catalog(file_path):
    
    path_array = file_path.split('/')
    path_array.remove('')

    try:
        path_array.remove('shared')
    except:
        pass

    
    try:
        path_array.remove('data')
    except:
        pass

    
    path_array = list(map(lambda x:x.lower(),path_array))
    current = ""
    parent = ""
    ancestors = ""
    
    for i in range(len(path_array)-1, -1 , -1):
        current = path_array[i]
        parent = path_array[i-1]
        ancestors = path_array[0:i-1]
        catalog_parent(file_path, current, parent)    
        dp_name = "../"+ parent+".html"
        if not os.path.isfile(dp_name):
            if i > 1:
                make_html(path_array[i-1], path_array[i-2], path_array[0:i-2])
            elif i ==1 :
                
                make_html(path_array[i-1])
        else:
            print(dp_name + ".html was already there")
        
        if i > 0:    
            link_to_children(current, parent)




def make_html(current, parent ="", ancestors=[]):

    catalog_dir = "https://raw.githubusercontent.com/kpegion/COLA-DATASETS-CATALOG/gh-pages/intake-catalogs/"
    open_catalog = catalog_dir + current +".yaml"
    title = current
    ancestors = '/'.join(ancestors)
    complete_ancestors = ancestors + parent + current
    cm =  []
    cm.extend([ancestors, parent])
    #pdb.set_trace()
    ancestors = make_ancestors('/'.join(cm))
    print("**********************************************************")
    print(ancestors)
    print("**********************************************************")

    _header = src_header(title, ancestors,  open_catalog)

    html_page = current +".html"

    with open(html_page , "w", encoding='utf-8') as file:
        file.write(_header)
        print( html_page + " was created\n")

    os.rename(html_page, "../"+html_page)




if __name__ == "__main__":
    fake_generate_catalog()

