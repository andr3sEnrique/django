from django.urls import path
from .views import morceau_detail, MorceauDetailView, MorceauList

app_name = 'musiques' # Encapsule les urls de ce module dans le namespace musique
urlpatterns = [
    path('<int:pk>', MorceauDetailView.as_view(), name='morceau_detail'),
    path('', MorceauList.as_view(), name='morceau_list'),
]