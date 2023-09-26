from django.urls import path
from . import views

urlpatterns=[
    path('home/<name>',views.home,name='home'),
    path('listing/', views.task_listing2,name="listing"),
    #path('details/',views.detail, name='detail'),
    path('email-details/<pk>',views.email_detail, name='email_detail'),
]