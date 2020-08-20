from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BooksAPI.as_view({'get': 'list'})),
    path('books/<int:pk>/', views.BookAPI.as_view()),

]

