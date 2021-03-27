# from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class PdfConvert(models.Model):
    name = models.CharField(max_length=255)
    pdfFile = models.FileField()

    def __str__(self):
        return self.name
