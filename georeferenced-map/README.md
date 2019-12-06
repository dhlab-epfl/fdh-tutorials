# Georeferenced map to leaflet

In this short tutorial, we will see how to use a geo-referenced TIF (e.g. obtained with [georeferencer](https://www.georeferencer.com)) and transform it into tiles that can be used directly with leaflet.

## Install gdal2tiles

The first step is to download `gdal2tiles` using pip:
```
pip install gdal2tiles
```

## Creating the tiles

We will now create tiles that can be directly used by leaflet from the TIF.

In the `data` folder there is an `example.tif` which contains a map of Paris.


```
cd data

gdal2tiles.py --processes=8 -z 11-16 example.tif tiles
```

It is possible to specify the output directory, here we chose `tiles`. We also specified the zoom extent. Here we chose between zoom levels 11-16 because the original image resolution is not very good. Be careful when choosing higher zoom level, because it will create much more images (4 tiles the images of the previous zoom level).

More options can be found in the [documentation](https://gdal.org/programs/gdal2tiles.html)

Once the script executed, it will create a new folder `tiles` (or what you chose as output directory name) which contains the tiles for each zoom level.

## Using the map with leaflet

The usage of the map with leaflet is very straightforward, we just need to add a new layer pointing to our tiles:
```
var geotiff_layer = L.tileLayer('data/tiles/{z}/{x}/{y}.png', {tms: true, opacity: 1.0, attribution: 'You should put the <a href="https://gallica.fr">gallica link here</a>', minZoom: 11, maxZoom: 22, minNativeZoom: 11, maxNativeZoom: 16}).addTo(map);
```

Note the options of `{min,max}Zoom` and `{min,max}NativeZoom`, we can set `{min,max}Zoom` to any values (usually the same as the basemap), but we should set the `{min,max}NativeZoom` to the actual levels we generated the tiles for (here 11-16), otherwise the map will not display at zoom levels outside of this range.

A working example is given in `index.html`.

