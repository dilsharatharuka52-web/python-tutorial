import shutil
import os

# 1. Create backup folder

os.makedirs("backup", exist_ok=True)


# 2. copy data.txt into backup

shutil.copy('data.txt', 'backup')

# 3. create ZIP archive

shutil.make_archive(
    "mybackup",
    "zip",
    root_dir="backup"
)