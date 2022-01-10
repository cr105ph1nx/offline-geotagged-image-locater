# Offline Geotagged-Image Locater

A webapp that locates any geotagged image file on a local, offline map within the constraint of the Algerian area. It uses the folium library.

## Project Setup

1- Cloning the project

```
$ git clone https://github.com/cr105ph1nx/offline-geotagged-image-locater
$ cd offline-geotagged-image-locater
```

2- Setting up a virtual environment

```
$ pip install virtualenv
$ virtualenv env
```

3- Activating environment on Linux

```
$ source env/bin/activate
```

4- Installing requirements

```
$ pip install -r requirments.txt
```

5- Adding XYZ raster map tiles to map-data/raster-tiles (You can roll the tiles using QGis)

6- Change map attributes in template/index.html

7- Open template/index.html
