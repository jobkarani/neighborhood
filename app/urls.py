from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    # path('join_hood/<int:id>', views.join_hood, name='join_hood'),
    # path('leave_hood/<int:id>', views.leave_hood, name='leave_hood'),

]
