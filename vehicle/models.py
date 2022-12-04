from django.db import models
# from PIL import Image

import PIL


# Create your models here.


CHOICES_CATEGORY = [
    ("",""),
    ("Saloon","Saloon"),
    ("Hatchback","Hatchback"),
    ("SUV","SUV"),
    ("Truck","Truck"),
    ("Caravan","Caravan"),

]

class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=90)
    regNo = models.CharField(max_length=90)
    model = models.CharField(max_length=90)
    category = models.CharField(choices = CHOICES_CATEGORY, default="", max_length=90 ,blank=True)
    accidentDescription = models.TextField(max_length=500)
    frontImage = models.ImageField(default='front.png', blank = True)
    sideImage1 = models.ImageField(default='side1.png', blank = True)
    sideImage2 = models.ImageField(default='side2.png', blank = True)
    rearImage = models.ImageField(default='rear.png', blank = True)
    dateReported = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-dateReported', '-dateReported')


    def __str__(self) -> str:
        return self.regNo

    # @property
    # def image_url(self):
    #     try:
    #         url = self.frontImage.url
    #         url = self.sideImage1.url
    #         url = self.sideImage2.url
    #         url = self.rearImage.url

    #     except:
    #         url = ''

    #     return url


