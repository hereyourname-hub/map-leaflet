import json
from django.shortcuts import render
from .models import Marker


def map_view(request):
    markers = Marker.objects.all()
    markers_json = json.dumps([{
        'name': marker.name,
        'address': marker.address,
        'latitude': marker.latitude,
        'longitude': marker.longitude
    } for marker in markers])
    context = {
        'markers_json': markers_json,
    }
    return render(request, 'map_app/map.html', context)

