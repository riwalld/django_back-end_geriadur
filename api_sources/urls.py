
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.crudSources),
    #path('<int:id>', views.getOne),
    #path('Str', views.getProtoCelticStrList),

]
