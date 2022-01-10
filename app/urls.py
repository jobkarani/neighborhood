from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('create_business', views.create_business, name='create_business'),
    # path('leave_hood/<int:id>', views.leave_hood, name='leave_hood'),

]
