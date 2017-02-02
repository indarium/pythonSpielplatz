import os, string
directory = 'DCIM'

available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
camList = []
for drive in available_drives:
    if os.path.exists('%s/%s'%(drive, directory)) == True:

        camList.append(drive)
        print('%s ist eine Kamera' %drive)
    else:
        print('%s is keine Kamera' %drive)



print(camList)
