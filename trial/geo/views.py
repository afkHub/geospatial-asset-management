from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse

from geojson import Feature, Point, FeatureCollection

from django.template import loader