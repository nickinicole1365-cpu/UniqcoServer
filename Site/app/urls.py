from app import views
from django.urls import path

urlpatterns =[
    path('home/',views.home,name='home'),
    path('ct/',views.Create_task),
    path('delete/<int:id>/', views.delete_task,name = 'delete'),
    path('edit/<int:id>/', views.edit_task, name='ed'),
    path('ver<int:id>',views.ver , name='ver_')
]