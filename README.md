# Offline Geotagged-Image Locater

This is my Operating System project for the first semester of Info-Sec Masters 1 at USTHB. 

A webapp that locates any geotagged image file on a local, offline map within the constraint of the Algerian area. It uses `flask` as a backend framework, the `leaflet.js` library to serve the map tiles dynamically, and `exifread` python module to extract metadata from images. The XYZ raster tiles were rolled using `QGIS`.

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
$ pip install -r requirements.txt
```

5- Run app

```
$ flask run
```
6- You can visit your app on any browser at `http://127.0.0.1:5000/`

## Customize the project 

- Add your personal XYZ raster map tiles to `sstatic/raster-tiles` (You can roll the tiles using QGIS)

- Customize your map attributes in `static/js/main.py`

