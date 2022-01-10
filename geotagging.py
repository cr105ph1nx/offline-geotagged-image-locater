import exifread
from sys import argv


def extractData(img):
    f = open(img, 'rb')
    tags = exifread.process_file(f)

    # d = map(str(tags['GPS GPSLatitude']).split(),int)
    d = str(tags['GPS GPSLatitude'])[1:-1].split(',')[:-1]
    north_south = -1 if (str(tags['GPS GPSLatitudeRef']) == "S") else 1

    d2 = str(tags['GPS GPSLongitude'])[1:-1].split(',')[:-1]
    east_west = -1 if (str(tags['GPS GPSLatitudeRef']) == "W") else 1

    for i, item in enumerate(d):
        d[i] = float(item)

    for i, item in enumerate(d2):
        d2[i] = float(item)

    lat = north_south*(d[0] + d[1]/60)
    lon = east_west*(d2[0] + d2[1]/60)
    # print (d, degrees)
    return tags, lat, lon


def saveData(tags, lat, lon):
    # Appending the following tags to the output file:
    accepted_tags = ["Image Orientation", "Image ResolutionUnit", "Image DateTime",
                     "EXIF ExifImageWidth", "EXIF ExifImageLength", "EXIF LensModel"]
    for tag in tags.keys():
        for accepted_tag in accepted_tags:
            if tag.startswith(accepted_tag):
                with open(f'exifdata/test.txt', "a") as file:
                    file.write("%s:%s\n" % (tag, tags[tag]))

    # Append latitude, longitude
    with open(f'exifdata/test.txt', "a") as file:
        file.write(f'GPS Latitude: {lat}\n')
        file.write(f'GPS Longitude: {lon}\n')


if __name__ == '__main__':
    img = str(argv[1])
    tags, lat, lon = extractData(img)
    saveData(tags, lat, lon)
