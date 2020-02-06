import os
import shutil
import photo_sync as sync

if __name__=='__main__':
    if os.path.isdir("test"):
        shutil.rmtree("test")
    shutil.copytree("raw", "test")
    
    sync.sync_dir("test/a", "test/b")