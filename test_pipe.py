import subprocess as S
import os,re
#res = S.run('ls -lrt --time-style=+%Y-%m-%d %H:%M:%S %4Z" | tail -n 1' , shell=True, stdout=S.PIPE, stderr=S.STDOUT, universal_newlines=True)

des_dir="/project/airsea/AVISO/"
cmd = "ls -lrt --time-style=+%Y-%m-%d " + str(des_dir) + " | tail -n 1"
ps = S.Popen(cmd,shell=True,stdout=S.PIPE,stderr=S.STDOUT, universal_newlines=True)
output = ps.communicate()[0]

res = re.findall(r'\d{4}-\d{2}-\d{2}', output)
print('\n'.join(res))

#print(output[40:50])





