from django.urls import path
from . import  views
urlpatterns=[
    path('',views.contact,name='contact'),
    path('details/',views.detail, name='detail'),
    path('email-details/',views.email_detail, name='email_detail')
]