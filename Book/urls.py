from django.urls import path
from Book import views


urlpatterns = [
    path('book/', views.book_info, name='book-info'),
    path("", views.home, name= 'home')
]