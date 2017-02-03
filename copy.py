import os, sys, re, string, pyexiv2, shutil


source = 'C:/DCIM/D_Test/DSC_1.jpg'
dest = 'C:/Users/paull/Documents/'

def copy( source, dest):

 cfile = os.path.basename(source)
 destfile = os.path.join(dest, cfile)
 if os.path.exists(destfile) == False:
    shutil.copy2(source, dest)
    sourceStat = os.stat(source)
    destStat = os.stat(destfile)
    if destStat.st_size == sourceStat.st_size:
        os.remove(source)
        print('File erfolgreich kopiert')
    else:
        print('Kopiervorgang fehlgschlagen')
 else:
     print('File bereits vorhanden')



copy(source, dest)
