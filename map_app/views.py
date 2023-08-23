from django.shortcuts import render
from .models import Marker
from django.core.serializers import serialize


def map_view(request):
    markers = serialize('json', Marker.objects.all())
    context = {
        'markers_json': markers,
    }
    return render(request, 'map_app/map.html', context)
