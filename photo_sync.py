import os
import cv2
import shutil

class Sync_set:
    def __init__(self):
        self.valid=set()
        self.invalid=set()

def is_file_valid(file):
    print(f"read {file}")
    return cv2.imread(file) is not None

def copy_file(src, dst):
    print(f"cp dst {dst}")
    shutil.copy(src, dst)

def is_img_file(file):
    return file.endswith(".jpg")

def comp_copy(src_dir, src_set, dst_dir, dst_set):
    for file in os.listdir(src_dir):
        file_src=os.path.join(src_dir, file)
        file_dst=os.path.join(dst_dir, file)
        
        if (os.path.isfile(file_src) and is_img_file(file) and file_src not in src_set.valid):
            if is_file_valid(file_src):
                src_set.valid.add(file_src)
                
                if file_dst in dst_set.invalid:
                    copy_file(file_src, file_dst)
                else:
                    if not is_file_valid(file_dst):
                        copy_file(file_src, file_dst)
                dst_set.valid.add(file_dst)
            else:
                src_set.invalid.add(file_src)
                
        elif os.path.isdir(file_src):
            if not os.path.isdir(file_dst):
                os.mkdir(file_dst)
            comp_copy(file_src, src_set, file_dst, dst_set)

def sync_dir(dir_a, dir_b):
    print(f"sync_dir dir_a {dir_a} dir_b {dir_b}")
    set_a=Sync_set()
    set_b=Sync_set()
    comp_copy(dir_a, set_a, dir_b, set_b)
    comp_copy(dir_b, set_b, dir_a, set_a)
    
