from django.urls import path
from .views import index, student_add_update, student_list

urlpatterns = [
    path('', index, name='index'),
    path('student/', student_add_update, name="form"),
    path('list/', student_list, name="list"),
]