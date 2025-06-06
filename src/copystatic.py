import os
import shutil

def copy_files(src,dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    else:
        shutil.rmtree(dst)
        os.mkdir(dst)
    
    for file in os.listdir(src):
        src_path = os.path.join(src, file)
        dst_path = os.path.join(dst, file)
       
        if os.path.isfile(src_path):
            shutil.copy(src_path,dst)
        else:
            os.mkdir(dst_path)
            copy_files(src_path,dst_path)
   