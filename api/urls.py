from django.urls import path
from .views import HotelView,UpdateHotelView,CreateHotelView,RetrieveHotelView

urlpatterns = [
    path('',HotelView.as_view(),name='home'),
    path('update/<int:id>',UpdateHotelView.as_view()),
    path('create/<int:id>',CreateHotelView.as_view()),
    path('delate/<int:id>',RetrieveHotelView.as_view())
]

