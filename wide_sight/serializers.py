import sys
import utm
from rest_framework import serializers
from django.contrib.gis.geos import GEOSGeometry, Point
from rest_framework.reverse import reverse
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import sequences, panoramas, image_object_types, image_objects


class sequences_serializer(serializers.ModelSerializer):
    # creator_name = serializers.SerializerMethodField()
    # def get_creator_name(self,obj):
    #     return obj.creator_key.user.username
    class Meta:
        model = sequences
        read_only_fields = ('id', 'geom', 'shooting_data',)
        geo_field = "geom"
        fields = ('id', 'title', 'geom', 'shooting_data', 'note')
        extra_kwargs = {
        #     'creator_key': {'write_only': True}
         }
    
class panoramas_serializer(serializers.ModelSerializer):
    
    def get_utm_geom(self,obj):
        if obj.lon and obj.lat:
            
            utm_srid = get_utm_srid_from_lonlat(obj.lon,obj.lat)
            # utm_srid = 4326
            utm_easting, utm_northing, utm_zone_number, utm_letter = utm.from_latlon(obj.lon,obj.lat)
            wgs84_geom =  GEOSGeometry(Point(utm_easting, utm_northing, srid=utm_srid), srid=utm_srid)
            return wgs84_geom.ewkt #wgs84_geom.transform(get_utm_srid_from_lonlat(obj.lon,obj.lat)).geojson
        else:
            return None

    # creator_name = serializers.SerializerMethodField()
    # def get_creator_name(self,obj):
    #     return obj.sequence.creator_key.user.username
    eqimage_thumbnail = serializers.ImageField(read_only=True)
    height_from_ground = serializers.SerializerMethodField()
    def get_height_from_ground(self,obj):
        return obj.height_correction or obj.sequence.height_from_ground

    class Meta:
        model = panoramas
        read_only_fields = ('id', 'utm_x', 'utm_y', 'utm_srid', 'utm_code', 'camera_prod', 'camera_model')
        fields = (
            'id',
            'eqimage',
            'eqimage_thumbnail',
            'geom',
            #'utm_geom',
            'sequence',
            'shooting_time',
            'lon',
            'lat',
            'utm_x',
            'utm_y',
            'utm_srid',
            'utm_code',
            'elevation',
            'accurancy',
            'heading',
            'height_from_ground',
            'height_correction',
            'pitch',
            'roll',
            'fov',
            'camera_prod',
            'camera_model',
            'address',
            'note'
        )

class panoramas_geo_serializer(GeoFeatureModelSerializer):

    # creator_name = serializers.SerializerMethodField()
    # def get_creator_name(self,obj):
    #     return obj.sequence.creator_key.user.username
    eqimage_thumbnail = serializers.ImageField(read_only=True)
    class Meta:
        model = panoramas
        read_only_fields = ('id', 'utm_x', 'utm_y', 'utm_srid', 'utm_code', 'camera_prod', 'camera_model')
        geo_field = "geom"
        fields = (
            'id',
            'eqimage',
            'eqimage_thumbnail',
            'geom',
            'sequence',
            # 'creator_name',
            'lon',
            'lat',
            'utm_x',
            'utm_y',
            'utm_srid',
            'utm_code',
            'elevation',
            'accurancy',
            'heading',
            'pitch',
            'roll',
            'fov',
            'camera_prod',
            'camera_model',
            'address',
            'note'
        )
class image_object_types_serializer(serializers.ModelSerializer):
    class Meta:
        model = image_object_types
        fields = ('type','pk', 'for_type', 'color')

class image_objects_serializer(serializers.ModelSerializer):

    # creator_name = serializers.SerializerMethodField()
    # def get_creator_name(self,obj):
    #     return obj.creator_key.user.username

    class Meta:
        model = image_objects
        #read_only_fields = ('creator', )
        fields = (
            'id',
            'type' ,
            # 'creator_name',
            # 'creator_key',
            'sample_type',
            'geom_on_panorama',
            'panorama',
            'match',
            'img_lat',
            'img_lon',
            'width',
            'height',
            'lon',
            'lat',
            'utm_x',
            'utm_y',
            'utm_code',
            'utm_srid',
            'elevation',
            'accurancy',
            'note',
            'user_data',
            'sampling_data',
        )
        extra_kwargs = {
            # 'creator_key': {'write_only': True}
        }

class image_objects_geo_serializer(GeoFeatureModelSerializer):
    # creator_name = serializers.SerializerMethodField()
    # def get_creator_name(self,obj):
    #     return obj.creator_key.user.username

    class Meta:
        model = image_objects
        #read_only_fields = ('creator', )
        geo_field = "geom"
        fields = (
            'id',
            'type' ,
            # 'creator_name',
            'sample_type',
            'geom_on_panorama',
            'panorama',
            'match',
            'img_lat',
            'img_lon',
            'width',
            'height',
            'lon',
            'lat',
            'utm_x',
            'utm_y',
            'utm_code',
            'utm_srid',
            'elevation',
            'accurancy',
            'note',
            'user_data',
            'sampling_data',
            'geom',
        )


