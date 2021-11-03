from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add_dojo',views.index2),
    path('add_ninja',views.index3),
    path('reset',views.index4),
    path('delete_dojo/<int:dojo_id>',views.delete_dojo),
]