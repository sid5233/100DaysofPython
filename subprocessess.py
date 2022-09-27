import cmd
import subprocess
cmd="ls -la"
##SHELL=TRUE
# sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
# rc=sp.wait()
# print(f'the return code {rc}')
# out,err=sp.communicate()
# print(f"Output is : \n{out.splitlines()}")
# print(f"Error is : \n{err}")

##SHELL=FALSE
cmd="['ls', '-la']"
sp = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
print(f'the return code {rc}')
out,err=sp.communicate()
print(f"Output is : \n{out.splitlines()}")
print(f"Error is : \n{err}")

# if shell=True then your cmd is string if shell=false then your cmd is list
  