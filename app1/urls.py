from django.urls import path
from app1.views import *
app_name='something1'
urlpatterns=[
    path('str1/',str1,name='str1'),
    path('str2/',str2,name='str2'),

]
