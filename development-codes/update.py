import json
import os
import yaml
import pdb



def update_json(tags, html_page, dataset_sub_name):
    if tags is None:
        return
    jp = open("../tags_hrefs.json","r")
    data = json.load(jp)
    print(tags)
    for tag in tags:
        addr = "https://kpegion.github.io/COLA-DATASETS-CATALOG/"+ html_page
        if tag in data:
            #print(dataset_sub_name)
            data[tag].append([dataset_sub_name, addr])
        else:
            data[tag] = [dataset_sub_name, addr]
    jp.close()
    jp = open("../tags_hrefs.json","w")
    json.dump(data,jp)
    jp.close()



def make_ancestors(ancestors):
    #<!-- 1qaz2wsx -->
    ancestors = ancestors.split('/')

    try:
        ancestors.remove('')
    except:
        pass

    

    try:
        ancestors.remove('shared')
    except:
        pass

    print(ancestors)
    print("------------------------------------------------------------------")

    try:
        ancestors.remove('data')

    except:
        pass

    #pdb.set_trace()

    #print(ancestors)
    #print("------------------------------------------------------------------")
    ancestors = list(map(lambda x:x.lower(),ancestors))
    #print(ancestors)
    #print("------------------------------------------------------------------")

    res = ""
    for i in range(len(ancestors)):
        res += "<li><a href="+ ancestors[i]+">"+ ancestors[i]+"</a></li>"
        res += "\n\n"

    #print(res)
    return res




def catalog_parent( _path, _dataset_name):

    print(_dataset_name) 
    direct_parent = _path.split('/')[-2].lower()
    dict_file = [
    {'description': 'COLDA '+ direct_parent.upper() + ' Data Caalog'},
    {'sources':{_dataset_name:[{'args':{'path':_path}},{'description':''},{'driver':'intake.catalog.local.YAMLFileCatalog'},{'metadata':'{}'}]
    }}]
    direct_parent = direct_parent + '.yaml'
    with open(direct_parent, 'a') as fp:
        yaml.dump(dict_file, fp)
        print(direct_parent + " created")



def catalog_parent_2( _path, _dataset_name, direct_parent):

    direct_parent = direct_parent + '.yaml'
    if not os.path.isfile(direct_parent):
     
        
        dict_file = [
        {'description': 'COLDA '+ direct_parent.upper() + ' Data Caalog'},
        {'sources':{_dataset_name:[{'args':{'path':_path}},{'description':''},{'driver':'intake.catalog.local.YAMLFileCatalog'},{'metadata':'{}'}]
        }}]

    
        with open(direct_parent, 'w') as fp:
            yaml.dump(dict_file, fp)
            print(direct_parent + " created")
        
    else:
        
        with open(direct_parent) as fp:
            newdct = yaml.load(fp, Loader=yaml.FullLoader)

        with open(direct_parent, 'w') as fp:
            newdct[1]['sources'][_dataset_name+"tesdgdghdghtak"] =[{'args':{'path':_path}},{'description':'JadidTar'},{'driver':'intake.catalog.local.YAMLFileCatalog'},{'metadata':'{}'}]
            yaml.dump(newdct, fp)

def link_to_children(child, dp_name):

    
    searchee = "<!--qazwsxxswzaq-->"
    res = """<a href="""+ "\""+ child+"\""+""" class="list-group-item">
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
