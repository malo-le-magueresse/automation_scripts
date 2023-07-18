import os 
import shutil
from constants import * 

# Change directory to Downloads
os.chdir(DOWNLOADS_PATH)

# Create the display message, making sure that we can track every file that is moved ; and then move the file
def display_message_and_move(name, path, target):
    print("--------------------")
    print("Moving: " + name)
    print("Old path:" + path)
    print("New path: " + target+name)
    print(".\n")
    shutil.move(path, target+name)

# Iterate over all the files in our Downloads folder
with os.scandir() as iterator:

    for document in iterator:

        path = document.path
        name = document.name
        
        # For now, we only move documents. Folders will wait
        if document.is_file() and document.name != '.DS_Store': # We do not want to move the .DS_Store file, which stores custom attributes of our Downloads folder (e.g., folder view options)
            
            document_extension = os.path.splitext(document.path)[1]

            # Whether the entry was moved
            flag = False

            for target, extensions in target_dir.items():
                for extension in extensions:
                    # As soon as we find the extension, we break the loop: we know where to move the file
                    if extension == document_extension:
                        flag = True 
                        target = target
                        break
                # Exit the loop if we found the extension
                if flag: 
                    break
            # If we haven’t found the extension for the file, we move it to the catch-all folder, OTHER_PATHS
            if not flag:
                target = OTHER_PATHS

        elif document.name != '.DS_Store' and document.name != 'Sorted downloads': # We do not want to move the "Sorted downloads" folder, which stores all the sorted files
            path = document.path
            name = document.name
            target = DIR_PATHS
        
        try:
            # Display the message and move the document
            display_message_and_move(name, path, target)
        except: 
            print("Error moving: " + name)
            print("Old path:" + path)