import fnmatch
import shutil
import os

result = []

for root, dirs, files in os.walk('/media/viki/8396777e-3c50-4169-b6b4-45aecff75027/backup'):
    for name in files:
        if fnmatch.fnmatchcase(name.lower(),'*.pdf'):
            result.append(os.path.join(root,name))
            #result.append(name)            
            #shutil.move(os.path.join(root,name),'/media/viki/8396777e-3c50-4169-b6b4-45aecff75027/JavascriptBooks/'+name)


print((result))