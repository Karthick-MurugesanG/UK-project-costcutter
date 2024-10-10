import os
import stat
import time

# Get the home directory
home_directory = os.path.expanduser("~")

# List all files in the home directory and their properties
files = [f for f in os.listdir(home_directory) if os.path.isfile(os.path.join(home_directory, f))]

print("File properties in the home directory:")
for file in files:
    file_path = os.path.join(home_directory, file)
    file_stat = os.stat(file_path)
    
    # Get file properties
    file_size = file_stat.st_size  # Size in bytes
    file_mtime = time.ctime(file_stat.st_mtime)  # Last modified time
    file_atime = time.ctime(file_stat.st_atime)  # Last accessed time
    file_ctime = time.ctime(file_stat.st_ctime)  # Creation time (or metadata change time)
    file_permissions = stat.filemode(file_stat.st_mode)  # File permissions
    
    # Print file properties
    print(f"File: {file}")
    print(f"  Size: {file_size} bytes")
    print(f"  Last modified: {file_mtime}")
    print(f"  Last accessed: {file_atime}")
    print(f"  Creation time: {file_ctime}")
    print(f"  Permissions: {file_permissions}")
    print("-" * 40)  # Separator for better readability


