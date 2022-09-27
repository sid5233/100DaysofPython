import cmd
import subprocess
cmd="ls -lrt"
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
rc=sp.wait()
print(f'the return code {rc}')
out,err=sp.communicate()
print(f"Output is : \n{out}")
print(f"Error is : \n{err}")
