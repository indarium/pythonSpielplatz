import os, sys, re, string, pyexiv2, shutil



def search(path):
    filetype = '.jpg'
    fileslist = []
    if os.path.isdir(path):
        elements = os.listdir( path )
        for element in elements:
            currentElement = os.path.join(path, element)
            if os.path.isdir(currentElement)==False:
                  fileslist.append(currentElement)
            else:
                fileslist = fileslist + search(currentElement)
    return fileslist

def dirSearch():
    directory = 'DCIM'

    available_drives = ['%s:/' % d for d in string.ascii_uppercase if os.path.exists('%s:/' % d)]
    camList = []
    for drive in available_drives:
        if os.path.exists('%s/%s'%(drive, directory)) == True:

            camList.append(os.path.join(drive, directory))
            print('%s ist eine Kamera' %drive)
        else:
            print('%s is keine Kamera' %drive)
    return camList

def Exif(iPath):
    metadata = pyexiv2.ImageMetadata(iPath)
    metadata.read()
    # Alle keys anzeigen
    metadata.exif_keys

    # Blende anzeigen
    tagNr = metadata['Exif.Photo.FNumber']
    print tagNr.raw_value
    # Verschlusszeit anzeigen
    tagExp = metadata['Exif.Photo.ExposureTime']
    print tagExp.raw_value
    # ISO anzeigen
    tagISO = metadata['Exif.Photo.ISOSpeedRatings']
    print tagISO.raw_value
    # Kameramodel anzeigen
    tagMdl = metadata['Exif.Image.Model']
    print tagMdl.raw_value
    # Aufnahmedatum anzeigen
    tagTime = metadata['Exif.Image.DateTime']
    print tagTime.value.year
    print tagTime.raw_value


def copy(source, dest):
    dest = 'C:/Users/paull/Documents/'
 #if os.path.exists(dest) == False:
    print(dest)
    print(source)
    shutil.copy2(source, dest)
    sourceStat = os.stat(source)
    destStat = os.stat(dest)
    #if destStat.st_size == sourceStat.st_size:
    os.remove(source)
    print('File erfolgreich kopiert')
    #else:
        #print('Kopiervorgang fehlgschlagen')
 #else:
#     print('File bereits vorhanden')




for dir in dirSearch():
 #path = dir
 #fl = []
 files = search(dir)
 for file in files:
   print file
   Exif(file)
   copy(file, '')
