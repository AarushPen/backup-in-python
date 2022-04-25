import os
import shutil
source="C:/Users/lperi/OneDrive/Desktop/C39/images"
destination="C:/Users/lperi/OneDrive/Desktop/Backup/"
files=os.listdir(source)
print(files)
shutil.move(source,destination)
