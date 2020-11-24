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
    

    
    try:
        file_path = file_path.replace("/day/day/","/day/")

    except:
        pass


    
    try:
        file_path = file_path.replace("/mon/Amon/","/mon/")

    except:
        pass



    try:
        file_path = file_path.replace("/mon/OImon/","/mon/")

    except:
        pass



    try:
        file_path = file_path.replace("/mon/Lmon/","/mon/")

    except:
        pass


    try:
        file_path = file_path.replace("/mon/LImon/","/mon/")

    except:
        pass



    try:
        file_path = file_path.replace("/mon/Omon/","/mon/")

    except:
        pass


    file_path = file_path.rstrip("\r")
    path_array = file_path.split('/')

    try:
        path_array.remove('')
    except:
        pass

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
    

    ans = []
    my_str = ""
    for i in range(len(path_array)-1):
        if len(my_str)>0:
            my_str = my_str + '_'
        my_str = my_str + path_array[i]
        ans.append(my_str)
    ans.append(path_array[-1])
    path_array = ans
    
    for i in range(len(path_array)-1, 0 , -1):
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
        #todo else:
            #todo print(dp_name + ".html was already there")
        
        if i > 0 and i != len(path_array)-1 :    
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
    print(cm)
    ancestors = make_ancestors('/'.join(cm), 0)
    print("&&&&&&&&&&&&&&&&&")
    _header = src_header(title, ancestors,  open_catalog)

    html_page = current +".html"

    with open(html_page , "w", encoding='utf-8') as file:
        file.write(_header)
        print( html_page + " was created\n")

    os.rename(html_page, "../"+html_page)




if __name__ == "__main__":
    fake_generate_catalog()

