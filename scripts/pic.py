import os
import shutil
if os.path.exists(special://homw/temp):
        log("shutil.rmtree Removing path")
        shutil.rmtree(special://home/temp, ignore_errors=true)