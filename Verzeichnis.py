import os, sys
path = "c:/Test"

def search(path):
    fileslist = []
    if os.path.isdir(path):
        elements = os.listdir( path )
        for element in elements:
            currentElement = os.path.join(path, element)
            if os.path.isdir(currentElement)==False:
                fileslist.append(currentElement)
            else:
    return fileslist

search(path)
for file in fileslist:
    print file
