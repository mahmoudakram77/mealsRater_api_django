from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator , MinValueValidator


# uuid


class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=23, null=False)
    description = models.TextField(max_length=360 , null=False) 

    def no_of_rating(self):
        ratings = Rating.objects.filter(meal=self)
        return len(ratings)
    def avg_rating(self):
        ratings = Rating.objects.filter(meal=self)
        total_stars = sum(rating.stars for rating in ratings)
        if len(ratings) > 0:
            return total_stars / len(ratings)
        else:
            return 0

    def __str__(self):
        return self.title
    
class Rating(models.Model):
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    # def __str__(self):
    #     return f"{self.meal.title} - {self.user.username}"
    

    class Meta:
        # اليوزر لا يستطيع ان يعمل ريت اكثر من مرة لنفس الوجبة
        unique_together = (('user', 'meal'))
        index_together = (('user','meal'),)