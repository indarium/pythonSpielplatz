import pyexiv2


def Exif(iPath):
metadata = pyexiv2.ImageMetadata('iPath')
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
