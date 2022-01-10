import exifread
import os


def extractData(img):
    f = open(img, 'rb')
    tags = exifread.process_file(f)

    # d = map(str(tags['GPS GPSLatitude']).split(),int)
    d = str(tags['GPS GPSLatitude'])[1:-1].split(',')[:-1]

    north_south = -1 if (str(tags['GPS GPSLatitudeRef']) == "S") else 1

    d2 = str(tags['GPS GPSLongitude'])[1:-1].split(',')[:-1]

    east_west = -1 if (str(tags['GPS GPSLatitudeRef']) == "W") else 1

    for i, item in enumerate(d):
        try:
            d[i] = float(item)
        except:
            d[i] = float(int(d[i].split('/')[0])/int(d[i].split('/')[1]))

    for i, item in enumerate(d2):
        try:
            d2[i] = float(item)
        except:
            d2[i] = float(int(d2[i].split('/')[0])/int(d2[i].split('/')[1]))

    lat = north_south*(d[0] + d[1]/60)
    lon = east_west*(d2[0] + d2[1]/60)
    # print (d, degrees)
    return tags, lat, lon


def saveData(tags, lat, lon):
    # Appending the following tags to the output file:
    exif_data_image = {"Image DateTime": [], "EXIF ExifImageWidth": [
    ], "EXIF ExifImageLength": [], "GPS Latitude": [], "GPS Longitude": []}
    # Appending the following tags to the output file:
    accepted_tags = ["Image DateTime",
                     "EXIF ExifImageWidth", "EXIF ExifImageLength"]
    for tag in tags.keys():
        for accepted_tag in accepted_tags:
            if tag.startswith(accepted_tag):
                # add to dictionary
                exif_data_image[tag].append(str(tags[tag]))

    # Append latitude, longitude to dictionary
    exif_data_image["GPS Latitude"].append(lat)
    exif_data_image["GPS Longitude"].append(lon)

    return exif_data_image


def getLocation(exif_data_image, path_to_image):
    template = f"""<h3 > ({exif_data_image['GPS Latitude']}, {exif_data_image['GPS Longitude']}) < /h3 ><p > {exif_data_image['Image DateTime']} < /p ><p > ({exif_data_image["EXIF ExifImageWidth"]}, {exif_data_image["EXIF ExifImageLength"]}) px< /p ><div style = "text-align:center" ><img width = "150" height = "150"src = "{path_to_image}"/></div >"""
    location = [template, exif_data_image['GPS Latitude'][0],
                exif_data_image['GPS Longitude'][0]]
    return location


def geotagging(UPLOAD_FOLDER):
    directory = os.listdir(UPLOAD_FOLDER)
    locations = []
    # iterate through images
    for image in directory:
        tags, lat, lon = extractData(f"{UPLOAD_FOLDER}/{image}")
        exif_data_image = saveData(tags, lat, lon)
        location = getLocation(exif_data_image, f"{UPLOAD_FOLDER}/{image}")
        locations.append(location)
    return locations
