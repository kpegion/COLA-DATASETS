import json
import os
import yaml

def update_json(tags, html_page, dataset_sub_name):
    if tags is None:
        return
    jp = open("../tags_hrefs_test.json","r")
    data = json.load(jp)
    print(tags)
    for tag in tags:
        addr = "https://kpegion.github.io/COLA-DATASETS-CATALOGGGGG/"+ html_page
        #print(dataset_sub_name)
        #print(type(dataset_sub_name))
        data[tag].append([dataset_sub_name, addr])
        #print(data[tag])
        #print("##########################################################")
    jp.close()
    jp = open("../tags_hrefs_test.json","w")
    json.dump(data,jp)
    jp.close()



def update_parents(ancestors):
    #<!-- 1qaz2wsx -->
    
    ancestors = ancestors.split('/')
    ancestors.remove('')
    try:
        ancestors.remove('shared')
    except:
        pass


    try:
        ancestors.remove('data')

    except:
        pass


    ancestors = list(map(lambda x:x.lower(),ancestors))


    res = ""
    for i in range(len(ancestors)):
        res += "<li><a href="+ ancestors[i]+">"+ ancestors[i]+"</a></li>"
        res += "\n\n"

    #print(res)
    return res





def insert_links(direct_parent):
    
    dp_name = direct_parent+".html"
    searchee = "<!--qazwsxxswzaq-->"
    res = """               <a href="precip.pentad.mean.nc" class="list-group-item"> 
                        <h4>cmap_pentad</h4> 
                        <p class="description"> </p> 
                    </a> """
    res = res + "\n\n" + searchee
    fp = open(dp_name, "rt")
    fin = fp.read()
    data = fin.replace(searchee, res)
    fp.close()

    fp = open(dp_name, "wt")
    fp.write(data)
    fp.close()      
    



def catalog_parent( _path, _dataset_name):


    direct_parent = _path.split('/')[-2].lower()
    dict_file = [
    {'description': 'COLDA '+ direct_parent + ' Data Caalog'},
    {'sources':{_dataset_name:[{'args':{'path':_path}},{'description':''},{'driver':'intake.catalog.local.YAMLFileCatalog'},{'metadata':'{}'}]
    }}]
    with open('direct_parent.yml', 'w') as fp:
        #print(os.path.abspath(direct_parent))
        yaml.dump(dict_file, fp)
        #os.rename('direct_parent.yml','direct_parent.yaml')

    cmd = 'mv direct_parent.yml direct_parent.yaml'
    os.system(cmd)
def update_links(child, dp_name):

    searchee = "<!--qazwsxxswzaq-->"
    res = """               <a href="""+ "\""+ child+"\""+""" class="list-group-item">
                    <h4>""" +child+ """</h4>
                    <p class="description"> </p>
                </a> """
    file_name = dp_name + ".html"
    res = res + "\n\n" + searchee 
    file_name = os.path.join( os.getcwd(), '..', file_name )
    fp = open(file_name, "r+")
    fin = fp.read()
    data = fin.replace(searchee, res)
    fp.seek(0,0)
    fp.write(data)
























