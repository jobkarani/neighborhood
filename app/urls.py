from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/profile/', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profiles/', views.profiles, name='profiles'),
    path('search/', views.search, name='search'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('create_business', views.create_business, name='create_business'),
    path('busineses/', views.busineses, name='busineses'),
    path('create_neighbourhood', views.create_neighbourhood,
         name='create_neighbourhood'),
    path('neighbourhood/', views.neighbourhood, name='neighbourhood'),
    path('join_hood/<int:id>', views.join_hood, name='join_hood'),
    path('leave_hood/<int:id>', views.leave_hood, name='leave_hood'),
    path('create_post', views.create_post, name='create_post'),
    path('post/', views.post, name='post'),
    # path('busineses/', views.busineses, name='busineses'),

]
