from django.urls import path
from . import views

urlpatterns=[
path('', views.mail1),
path('mail2/', views.mail2),
path('mail2/', views.mail3),

]


