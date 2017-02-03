import os, sys, re, string, pyexiv2, shutil

cfile = ''
source = 'C:/Test/DSC_1332.jpg'
dest = 'C:/Users/paull/Documents/'
def copy(cfile, source, dest):

 if os.path.exists(dest) == False:
    shutil.copy2(source, dest)
    sourceStat = os.stat(source)
    destStat = os.stat(dest)
    if destStat.st_size == sourceStat.st_size:
        os.remove(source)
        print('File erfolgreich kopiert')
    else:
        print('Kopiervorgang fehlgschlagen')
 else:
     print('File bereits vorhanden')



copy(source, dest)
