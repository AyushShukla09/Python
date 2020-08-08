import subprocess
str="java -version"
sp=subprocess.Popen(str,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()
if rc==0 :
    if bool(o)==False and bool(e)==True :
        print(e.split()[2].strip("\""))
else:
    print(f'command was failed and error was {e} ')

