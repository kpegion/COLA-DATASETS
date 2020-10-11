import json
import os
import yaml



def make_html(current, parent, ancestors):
    
    catalog_dir = "https://raw.githubusercontent.com/kpegion/COLA-DATASETS-CATALOG/gh-pages/intake-catalogs/"
    open_catalog = catalog_dir + current +".yaml"
    title = current

    _header = src_header(title, ancestors,  open_catalog)

    html_page = current +".html"

    with open(html_page , "w", encoding='utf-8') as file:
        file.write(_header)
        print( html_page + " was created\n")




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





    



def catalog_parent( _path, _dataset_name):

    
    direct_parent = _path.split('/')[-2].lower()
    dict_file = [
    {'description': 'COLDA '+ direct_parent + ' Data Caalog'},
    {'sources':{_dataset_name:[{'args':{'path':_path}},{'description':''},{'driver':'intake.catalog.local.YAMLFileCatalog'},{'metadata':'{}'}]
    }}]
    
    direct_parent = direct_parent + '.yaml'
    with open(direct_parent, 'w') as fp:
        yaml.dump(dict_file, fp)

def update_links(child, dp_name):

    searchee = "<!--qazwsxxswzaq-->"
    res = """               <a href="""+ "\""+ child+"\""+""" class="list-group-item">
                    <h4>""" +child+ """</h4>
                    <p class="description"> </p>
                </a> """

    
    file_name = dp_name + ".html"
    res = res + "\n\n" + searchee

    fp = open('../'+file_name, "r+")
    fin = fp.read()
    data = fin.replace(searchee, res)
    fp.seek(0,0)
    fp.write(data)

