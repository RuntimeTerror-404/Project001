# from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from .serializers import PdfConvertSerializer
from .models import PdfConvert
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


class PdfConvertViewset(viewsets.ModelViewSet):
    queryset = PdfConvert.objects.all()
    serializer_class = PdfConvertSerializer
