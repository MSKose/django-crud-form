from django.urls import path
from .views import student_add_update, student_list, student_delete

urlpatterns = [
    # path('', home, name='home'),
    path('', student_add_update, name="form"),
    path('<int:id>/', student_add_update, name="update"),
    path('list/', student_list, name="list"),
    path('delete/<int:id>/', student_delete, name="delete"),
]