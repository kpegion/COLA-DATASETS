import os

def generate_directory_tree(dir_path):
    paths = []
    for root, _, files in os.walk(dir_path):
        paths.append(root)
        paths.extend(os.path.join(root,) for _file in files)
    paths = set(paths)
    return paths



#paths = generate_directory_tree('/homes/nbehboud/test')
paths = generate_directory_tree('/shared/subx/forecast')
paths = sorted(list(paths))[1:]
#print(generate_directory_tree('/homes/nbehboud/test'))

for path in paths:
    path = path.replace('/shared/subx/forecast','/homes/nbehboud/ppp')
    print(path)
    os.mkdir(path)
