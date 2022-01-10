from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('join_hood/<int:id>', views.join_hood, name='join_hood'),
    path('leave_hood/<int:id>', views.leave_hood, name='leave_hood'),

]
