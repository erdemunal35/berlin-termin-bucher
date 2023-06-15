import subprocess 
import sys 
 
for scriptInstance in [1,2,3]: 
    sys.stdout=open('result%s.txt' % scriptInstance,'w') 
    subprocess.check_call(['python','selenium-trial.py'], stdout=sys.stdout, stderr=subprocess.STDOUT)
