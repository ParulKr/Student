
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_show, name='addshow'),
    path('delete/<int:pk>/', views.delete_stu, name='delete'),
    path('update/<int:pk>/', views.update_stu, name='update'),
]
