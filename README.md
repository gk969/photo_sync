# photo_sync

## Usage
Sync photo files in the directory "dir_a" and "dir_b" 
```
import photo_sync as sync

sync.sync_dir("dir_a", "dir_b")
```

## Features
* Sync the file that exist in one directory but not exist in another directory
* Sync the file that damaged in one directory but not damaged in another directory
* Support subdirectory