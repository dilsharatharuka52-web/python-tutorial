import subprocess
# subprocess.run('dir', shell = True)
subprocess.run(['cmd', '/c', 'dir'])

with open('output.txt', 'w') as f:
    pi = subprocess.run(['cmd', '/c', 'dir'],stdout=f, text=True )


