import os
print(os.getcwd()) # get curent working directry

#os.chdir('C:\\Users\\Tharuka\\Desktop') # change file path
print(os.getcwd())
print(os.listdir()) # list file and folder in destop

# create direactry

# os.mkdir('os-demo-1') # intermideat level
os.makedirs('os-demo-2/new') # deep level this one can sub directry


# delect directry

# os.rmdir('os-demo-1') # this one is delect  intermidiat one
os.removedirs('os-demo-2/new') # deep level this one can sub directry delect


# rename folder

#os.rename('new.txt', 'car.txt')
print(os.listdir()) 

# working directery tree

# for dirpath, dirname, filename in os.walk('C:\\Users\\Tharuka\\Desktop'):
#     print('current path', dirpath)
#     print('directories', dirname)

# get env variable
#print(os.environ)


# join path
path1 = 'C:\\Users\\Tharuka\\Desktop'
path2 = 'Python'
path3 = 'os.py'

filepath = os.path.join(path1, path2,path3)

print(filepath)
