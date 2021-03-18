from django.db import models

# Create your models here.

from django.contrib.gis.db import models

class AssetTypeSymbol(models.Model):
    name = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)


class AssetType(models.Model):
    name = models.CharField(max_length=22)
    description = models.TextField(blank=True, null=False)
    industry = models.CharField(max_length=22)
    symbol = models.ForeignKey(AssetTypeSymbol, null=True, on_delete= models.CASCADE)

    def __str__(self):
        return self.name


class Asset(models.Model):
    assetTypeID = models.ForeignKey(AssetType, on_delete= models.CASCADE)
    name = models.CharField(max_length=22)
    lon = models.FloatField()
    lat = models.FloatField()
    #objects = models.GeoManager()
    elevation = models.FloatField()
    crs = models.IntegerField(null=True)
    geom = models.GeometryField(srid= 3857, blank= True, null=False)

    def __str__(self):
        return self.name


class AssetTypeProperties(models.Model):
    assetTypeID = models.ForeignKey(AssetType, on_delete= models.CASCADE)
    propertName = models.CharField(max_length=22)
    propertyType = models.CharField(max_length=15)


class AssetPropertyValues(models.Model):
    assetPropertyID= models.ForeignKey(AssetTypeProperties, on_delete= models.CASCADE)
    assetID = models.ForeignKey(Asset, null = True, on_delete= models.CASCADE)
    value = models.BooleanField(null=True) 
    name = models.CharField(max_length=22)


class Staffs(models.Model):
    name = models.CharField(max_length=22)
    surname = models.CharField(max_length=22)
    workAt = models.ForeignKey(Asset, null=True, on_delete= models.CASCADE)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    adress = models.CharField(max_length=500)
    rank = models.CharField(max_length=100)
