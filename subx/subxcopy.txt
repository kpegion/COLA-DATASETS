import os
import shutil

def automate(dir_adr):
    for root, dirs, files in os.walk(dir_adr):
        for filename in files:                
            
            old_name = os.path.join( os.path.abspath(root), filename )
            new_name = os.path.basename(os.path.dirname(old_name))+".txt" 
            adr = os.path.abspath(root)
            cwd = os.getcwd()
            adr = adr.replace(cwd,'/shared/subx')
            new_name = os.path.join( os.path.abspath(root), new_name )
            try:
                shutil.copy2(old_name, new_name)
                inp = open(new_name, 'r')
                lines = inp.read()
                inp.close()
                
                outp = open(new_name, 'w')
                lines2 = [adr+"/"+line for line in lines.split('\n')]
                for item in lines2:
                    outp.write('{}\n'.format(item))
                
                outp.close()
                
            except Exception as e:
                print(e)


automate('/homes/nbehboud/COLA-DATASETS-CATALOG/subx/forecast/prsfc')
automate('/homes/nbehboud/COLA-DATASETS-CATALOG/subx/forecast/psl')
automate('/homes/nbehboud/COLA-DATASETS-CATALOG/subx/forecast/rluttoa')
automate('/homes/nbehboud/COLA-DATASETS-CATALOG/subx/forecast/tas2m')
automate('/homes/nbehboud/COLA-DATASETS-CATALOG/subx/forecast/tssfc')
automate('/homes/nbehboud/COLA-DATASETS-CATALOG/subx/forecast/ua200')
automate('/homes/nbehboud/COLA-DATASETS-CATALOG/subx/forecast/ua850')
automate('/homes/nbehboud/COLA-DATASETS-CATALOG/subx/forecast/uas10m')
automate('/homes/nbehboud/COLA-DATASETS-CATALOG/subx/forecast/va200')
automate('/homes/nbehboud/COLA-DATASETS-CATALOG/subx/forecast/va850')
automate('/homes/nbehboud/COLA-DATASETS-CATALOG/subx/forecast/vas10m')
#automate('/homes/nbehboud/COLA-DATASETS-CATALOG/subx/forecast/zg200')
automate('/homes/nbehboud/COLA-DATASETS-CATALOG/subx/forecast/zg500')


