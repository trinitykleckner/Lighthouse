from django.urls import path

from . import views

app_name = "light_house"
urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:id>/',views.detail, name="detail")
]

