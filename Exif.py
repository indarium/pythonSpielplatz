import pyexiv2
metadata = pyexiv2.ImageMetadata('C:\Users\paull\Downloads\DSC_1332.jpg')
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

tagTime = metadata['Exif.Image.DateTime']
print tagTime.raw_value

tagTime2 = metadata['Exif.Photo.DateTimeOriginal']
print tagTime2.raw_value
