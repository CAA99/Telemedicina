import subprocess 
import time
def apagar():
    print('apagando')
    time.sleep(5)
    subprocess.Popen(['sudo', 'shutdown', '-h', 'now'])
if __name__ == '__main':
    
    apagar()