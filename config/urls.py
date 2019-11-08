from django.contrib import admin
from django.urls import path, include
from habit_tracker import views

urlpatterns = [
    path('accounts/', include('registration.backends.default.urls')),
    path('', views.home_page, name='home_page'),
    path('accounts/profile/', views.profile_page, name='profile_page'), 
    path('accounts/<int:pk>/habit_detail/', views.habit_detail, name='habit_detail'), 
    path('admin/', admin.site.urls),
]

