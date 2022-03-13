from django.db import models
from django.contrib.auth.models import User
import uuid
from geopy.geocoders import Nominatim

# Create your models here.

class UserLocations(models.Model):
    user = models.ForeignKey(User, related_name='user_locations', on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=100, default="")
    pincode = models.CharField(max_length=10, default="")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uuid

    def save(self, *args, **kwargs):
        # initialize Nominatim API
        geolocator = Nominatim(user_agent="geoapiExercises")
        # Latitude & Longitude input
        self.latitude = round(self.latitude, 3)
        self.longitude = round(self.longitude, 3)
        latitude = str(self.latitude)
        longitude = str(self.longitude)
        location = geolocator.reverse(latitude+","+longitude)
        address = dict(location.raw['address'])
        self.city = address.get('city', '')
        self.state = address.get('state', '')
        self.country = address.get('country', '')
        self.pincode = address.get('postcode', '')
        super(UserLocations, self).save(*args, **kwargs)