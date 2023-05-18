from django.urls import path
from .views import add_food, delete_food

app_name = 'app'

urlpatterns = [
    path('add_food/<int:food_id>', add_food, name='add_food'),
    path('delete_food/<int:id>', delete_food, name='delete_food'),

]