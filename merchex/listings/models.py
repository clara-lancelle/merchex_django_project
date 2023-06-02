# listings/models.py

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):

    def __str__(self):
        return f'{self.name}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
	
class Listing(models.Model):
    
    def __self__(self):
        return f'{self.title}'

    class Type(models.TextChoices):
        RECORD = 'RE'
        CLOTHING = 'CL'
        POSTERS = 'PO'
        MISCELLANEOUS = 'MI'

    band_fk = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    type = models.fields.CharField(choices=Type.choices, max_length=5)
    year = models.fields.IntegerField(null=True, 
    validators=[MinValueValidator(0), MaxValueValidator(2023)]
    )
    
