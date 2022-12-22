from django.urls import path
from Reader import views


urlpatterns = [
    path("", views.createUser, name='user')
]