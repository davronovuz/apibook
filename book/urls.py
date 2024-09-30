from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.ListBooksView.as_view()),
    path('create/',views.CreateBookView.as_view()),
    path('detail/<int:pk>/',views.DetailBookView.as_view()),
    path('update/<int:pk>/',views.UpdateBookView.as_view()),
    path('delete/<int:pk>/',views.DeleteBookView.as_view()),
]