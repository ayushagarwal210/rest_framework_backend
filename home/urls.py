from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', index, name="index"),
    # path('student', post_student, name="post_student"),
    # path('update-student/<id>', update_student, name="update_student"),
    # path('delete-student/<id>', delete_student, name="delete_student"),
    path('getbook', get_book, name="get_book"),
    path('student', StudentAPI.as_view()),
]
