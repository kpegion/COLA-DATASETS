import json
import os
import yaml
import pdb



def update_json(tags, html_page, dataset_sub_name):
    if tags is None:
        return
    jp = open("../tags_hrefs.json","r")
    data = json.load(jp)
    for tag in tags:
        addr = "https://kpegion.github.io/COLA-DATASETS-CATALOG/"+ html_page
        if tag in data:
            data[tag].append([dataset_sub_name, addr])
        else:
            data[tag] = [dataset_sub_name, addr]
    jp.close()
    jp = open("../tags_hrefs.json","w")
    json.dump(data,jp)
    jp.close()



def make_ancestors(ancestors):
    #<!-- 1qaz2wsx -->
    
    try:
        ancestors = ancestors.replace("/day/day/","/day/")

    except:
        pass


    
    try:
        ancestors = ancestors.replace("/mon/Amon/","/mon/")

    except:
        pass



    try:
        ancestors = ancestors.replace("/mon/OImon/","/mon/")

    except:
        pass




    try:
        ancestors = ancestors.replace("/mon/Lmon/","/mon/")

    except:
        pass





    try:
        ancestors = ancestors.replace("/mon/LImon/","/mon/")

    except:
        pass





    try:
        ancestors = ancestors.replace("/mon/Omon/","/mon/")

    except:
        pass




    ancestors = ancestors.split('/')

    try:
        ancestors.remove('')
    except:
        pass

    

    try:
        ancestors.remove('shared')
    except:
        pass

    try:
        ancestors.remove('data')

    except:
        pass

    #pdb.set_trace()

    
    ancestors = list(map(lambda x:x.lower(),ancestors))

    res = ""
    for i in range(len(ancestors)):
        if ancestors[i] != "":
            res += "<li><a href="+ ancestors[i]+">"+ ancestors[i]+"</a></li>"
            res += "\n\n"

    return res

def catalog_parent( _path, _dataset_name, direct_parent):

    direct_parent = direct_parent + '.yaml'
    rel_path_direct_parent = "../intake-catalogs/" + direct_parent
    yaml_path = "{{CATALOG_DIR}}/"+ _dataset_name + ".yaml"
    if not os.path.isfile(rel_path_direct_parent):

        dict_file = {
        'description': 'COLDA '+ direct_parent.replace('.yaml','').upper() + ' Data Caalog',
        'sources': {
        _dataset_name: {
            'args': {'path':yaml_path}, 
            'description':'', 
            'driver':'intake.catalog.local.YAMLFileCatalog', 
            'metadata':{}}}}
    
        with open(rel_path_direct_parent, 'w') as fp:
            yaml.dump(dict_file, fp)
            print(direct_parent + " now created")
        
    else:
        
        with open(rel_path_direct_parent) as fp:
            newdct = yaml.load(fp, Loader=yaml.FullLoader)

        with open(rel_path_direct_parent, 'w') as fp:
            newdct['sources'][_dataset_name] = { 'args': {'path':yaml_path}, 'description':'', 'driver':'intake.catalog.local.YAMLFileCatalog', 'metadata':{}}
            yaml.dump(newdct, fp)
            print(direct_parent + " updated")

def link_to_children(child, dp_name):

    
    searchee = "<!--qazwsxxswzaq-->"
    res = """<a href="""+ "\""+ child+ "\""+""" class="list-group-item">
                    <h4>""" +child+ """</h4>
                    <p class="description"> </p>
                </a> """
    
    #pdb.set_trace() 
    file_name = dp_name + ".html"

    fp = open('../'+file_name, "r+")
    fin = fp.read()

    if (fin.find(res) == -1): 
        res = res + "\n\n" + searchee
        data = fin.replace(searchee, res)
        fp.seek(0,0)
        fp.write(data)
    fp.close()
