import os
import shutil

# Create subdirectory (if it doesn't exist)
os.makedirs('new_folder', exist_ok=True)

# Copy file from source to new subdirectory
shutil.copy('source_folder/file.txt', 'new_folder/')
