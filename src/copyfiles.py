import os
import shutil

def delete_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"Removed dir succesfully: {path}")

def copy_all_files(source_dir, dest_dir):
    copied_files = os.listdir(source_dir)
    for file in copied_files:
        file_path = os.path.join(source_dir,file)
        if os.path.isdir(file_path):
            shutil.copytree(file_path,dest_dir+f"/{file}")
            print(f"Copied directory: {file_path} to {dest_dir}")
        else:
            shutil.copy(file_path, dest_dir)
            print(f"Copied file: {file_path} to {dest_dir}")
    
def generate(path):
    # deleting a directory if it exists
    delete_dir(os.path.join(path,"public"))
    # creating new dir to contain all the files
    os.mkdir(os.path.join(path,"public"))
    print(f"Created directory: {os.path.join(path,'public')}")
    # copy all the files from static to public
    copy_all_files(os.path.join(path,"static"), os.path.join(path,"public"))
