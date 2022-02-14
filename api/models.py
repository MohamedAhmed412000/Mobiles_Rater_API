import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Mobile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=10)
    price = models.IntegerField(validators=[MinValueValidator(0)])

    def no_of_ratings(self):
        ratings = Rating.objects.filter(mobile=self).aggregate(models.Count('stars'))
        return ratings["stars__count"]

    def avg_ratings(self):
        ratings = Rating.objects.filter(mobile=self).aggregate(models.Avg('stars'))
        if self.no_of_ratings() == 0:
            return 0
        return ratings["stars__avg"]

    def __str__(self):
        return f"{self.company} {self.name}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user} gives {self.mobile} {self.stars} stars."

    # This to make the user gives his rating to mobile only 1 time
    class Meta:
        unique_together = (('user', 'mobile'),)
        index_together = (('user', 'mobile'),)
