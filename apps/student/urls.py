from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_list, name='index'),
    path('new/', views.student_new, name="student_new"),
    path('update/<int:id>/', views.student_update, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
]
