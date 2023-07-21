from django.contrib import admin
from .models import Meal, Rating

# Register your models here.

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'username', 'stars']
    list_filter = ['meal', 'user']

    def title(self,rate_obj):
        return rate_obj.meal.title

    def username(self, user_obj):
        return user_obj.user.username

class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    search_fields = ['title', 'description']
    list_filter = ['title', 'description']

    def description(self, meal_obj):
        return meal_obj.description

admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)
