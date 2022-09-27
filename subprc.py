from asyncio import subprocess
import errno
from os import environ
import subprocess

cmd='echo ${HOME}'
sp=subprocess.Popen(cmd,shell=True, env=environ, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()

print(f'The return code :  {rc}')
print(f'The output : \n{out}')
print(f'The err : {err}')