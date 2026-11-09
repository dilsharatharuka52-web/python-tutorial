import shutil  # import shutil modul
# shutil is python module use mange file and folder

# copy file one to other

# shutil.copy('output.txt', 'new.txt') # This one use make a copy of an existing file.

# Explanation:
# - First argument: Original file.
# - Second argument: Destination file.
# - Python creates new.txt with the contents of output.txt

# shutil.copy2() – Copy with metadata

# shutil.copy2('output.txt', 'backup.txt') # this one use copy2() works like copy(), but it also attempts to preserve file metadata.

# Metadata means additional file information, such as:
# - Last modification time.
# - Access time.
# - Permission information.

# shutil.copyfile() - Copy only contents 
# shutil.copyfile('output.txt','car.txt')


# Difference:
# Function	Copies
# copy()	Contents + permission mode
# copy2()	Contents + attempts to preserve metadata
# copyfile()	Contents only




# Copy an entire folder - shutil.cpytree()

# shutil.copytree('source', 'backup') #  copy everything into backup


# Delete a folder - shutil.rmtree()

# shutil.rmtree('backup') # it use delete the entire backup folder


# Move a file - shutil.move() 

# shutil.move('car.txt', 'backup/')



# Create an archive - shutil.make_archive()

shutil.make_archive(
    'mybackup',  # Archive name
    'zip',       # Archive format
    root_dir='source' # Directory to archive
)  # it use to create a ZIP file from your source folder


shutil.unpack_archive(
    'mybackup.zip',
    'extracted'
)

# Check disk space - shutil.disk_usage()

usage = shutil.disk_usage('c:/')

print("Total :", usage.total)
print("Used :", usage.used)
print("Free :", usage.free)