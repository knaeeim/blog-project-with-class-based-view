from django.urls import path, include
from .views import *
urlpatterns = [
    path('add_categories/', add_categories, name="add_categories"),
]