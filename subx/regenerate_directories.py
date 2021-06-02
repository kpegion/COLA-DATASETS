import os
import pickle

def generate_directory_tree(dir_path):
    paths = []
    for root, _, files in os.walk(dir_path):
        paths.append(root)
        paths.extend(os.path.join(root,) for _file in files)
    paths = set(paths)
    return paths



#paths = generate_directory_tree('/shared/subx/forecast/prsfc/')
#paths = generate_directory_tree('/shared/subx/forecast/psl')
#paths = generate_directory_tree('/shared/subx/forecast/rluttoa/')
#paths = generate_directory_tree('/shared/subx/forecast/tas2m/')
#paths = generate_directory_tree('/shared/subx/forecast/tssfc/')
#paths = generate_directory_tree('/shared/subx/forecast/ua200/')
#paths = generate_directory_tree('/shared/subx/forecast/ua850/')
#paths = generate_directory_tree('/shared/subx/forecast/uas10m/')
#paths = generate_directory_tree('/shared/subx/forecast/va200/')
#paths = generate_directory_tree('/shared/subx/forecast/va850/')
paths = generate_directory_tree('/shared/subx/forecast/vas10m/')
#paths = generate_directory_tree('/shared/subx/forecast/zg200/')
#paths = generate_directory_tree('/shared/subx/forecast/zg500/')
paths = sorted(list(paths))[0:]

for path in paths:
    ls_dir = os.listdir(path)
    path_new = path.replace('/shared/subx/','/homes/nbehboud/ppp/')
    os.mkdir(path_new)
    files = path_new+"/files.txt"
    with open(files,'w') as fp:
       fp.write("\n".join(ls_dir))
