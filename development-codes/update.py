import json
import os
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

    print(res)
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
    



    




























