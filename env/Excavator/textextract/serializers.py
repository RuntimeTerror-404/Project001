from rest_framework import serializers
from .models import PdfConvert


class PdfConvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfConvert
        fields = '__all__'