
import os
import sys
import shutil #Shutil module allows you to do high-level operation on file such as copy, paste, and remove operations

def move_file(source_of_file):
    #Base case:
    if not os.path.exists(source_of_file):
        return("File source is not exist")
    else:
        for file in os.listdir(source_of_file): #File loop thorugh all file in a folder
            if file.startswith('.'):
                continue

            file_name, file_type = os.path.splitext(file)
            file_type = file_type[1:]

            #Create a temporary check directory
            check_path = os.path.join(source_of_file, file_type)

            #Check if folder is already exist
            if not os.path.isdir(check_path): #If the folder not exist
                new_path = os.makedirs(check_path, exist_ok=True) #Create a new folder

            #Move the file into the new folder
            shutil.move(os.path.join(source_of_file, file), os.path.join(check_path, file))



def main():
    sourcePath = "/Users/panda/Desktop/Test1"
    move_file(sourcePath)


if __name__ == "__main__":
    main()
