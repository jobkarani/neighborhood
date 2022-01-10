from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('create_business', views.create_business, name='create_business'),
    path('busineses/', views.busineses, name='busineses'),
    path('create_neighbourhood', views.create_neighbourhood,
         name='create_neighbourhood'),
    path('neighbourhood/', views.neighbourhood, name='neighbourhood'),
    path('join_hood/<int:id>', views.join_hood, name='join_hood'),
    path('leave_hood/<int:id>', views.leave_hood, name='leave_hood'),

    # path('busineses/', views.busineses, name='busineses'),

]
