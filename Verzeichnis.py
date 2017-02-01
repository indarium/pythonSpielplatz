import os, sys
path = "c:/Test"
fileslist = []
def search(path):

    if os.path.isdir(path):
        elements = os.listdir( path )
        for element in elements:
            currentElement = os.path.join(path, element)
            if os.path.isdir(currentElement)==False:
                fileslist.append(currentElement)
            else:
             search(currentElement)

search(path)
for file in fileslist:
    print file
