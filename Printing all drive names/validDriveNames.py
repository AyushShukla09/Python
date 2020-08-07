import string
import os
for drive in string.ascii_lowercase :
    if os.path.exists(drive+":\\") :
        print(drive+"\\:")
