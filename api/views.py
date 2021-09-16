from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-Update/',
    }
    return Response('API BASE POINT', safe = False)
