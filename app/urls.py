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
    # path('busineses/', views.busineses, name='busineses'),
    # path('busineses/', views.busineses, name='busineses'),

]
