from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    friends = models.ManyToManyField('User', blank=True)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)


class Vehicle(models.Model):
    TRANSPORT = (
        ('SM', 'Small, Medium, Compact'),
        ('SUV', 'Minivan or Small SUV'),
        ('BIG', 'Pickup, Large SUV, or Sports Car'),
        ('BUS', 'Bus & Public Transit'),
        ('RAIL', 'Rail'),
        ('PLN', 'Plane'),
        ('BIKE', 'Bycicle or Walk')
    )

    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50, choices=TRANSPORT)


    def __str__(self):
        return self.name


class Footprint(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='footprint', null=True)
    total = models.BigIntegerField()
    today = models.IntegerField()
    start = models.DateField(auto_now_add=True)
    monday = models.IntegerField()
    tuesday = models.IntegerField()
    wednesday = models.IntegerField()
    thursday = models.IntegerField()
    friday = models.IntegerField()
    saturday = models.IntegerField()
    sunday = models.IntegerField()

    def clearWeek(self):
        self.total = self.total + self.monday + self.tuesday + self.wednesday + self.thursday + self.friday + self.saturday + self.sunday
        self.monday = 0
        self.tuesday = 0
        self.wednesday = 0
        self.thursday = 0
        self.friday = 0
        self.saturday = 0
        self.sunday = 0

    def serialize(self):
        return {
            'id': self.id,
            'total': self.total,
            'today': self.today,
            'start': self.start,
            'monday': self.monday,
            'tuesday': self.tuesday,
            'wednesday': self.wednesday,
            'thursday': self.thursday,
            'friday': self.friday,
            'saturday': self.saturday,
            'sunday': self.sunday
        }



class Race(models.Model):
    start_date = models.DateField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='profile', blank=True, null=True)
    tracker = models.OneToOneField(Footprint, related_name='profile', on_delete=models.CASCADE, blank=True, null=True)
    race = models.ForeignKey(Race, related_name='profile', on_delete=models.CASCADE, blank=True, null=True)
    raceswon = models.IntegerField(blank=True, null=True)
    bonus = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}'s profile"
    