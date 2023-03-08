from django.urls import path
from tools import views
urlpatterns = [
    path('',views.index),
    path('scrapper',views.scrapper,name='scrapper'),
]
