import os
import shutil
from_dir="C:/Users/Dell/Downloads"
to_dir="C:/Users/Dell/Desktop"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for x in list_of_files:

    name, extension = os.path.splitext(x)
    print(name)
    print(extension)
