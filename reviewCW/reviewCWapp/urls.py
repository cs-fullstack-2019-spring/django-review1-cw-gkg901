from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('page2/<int:pageID>', views.page2, name='page2'),
    path('page3/<int:pageID>', views.page3, name='page3'),
    path('page4/<int:pageID>', views.page4, name='page4'),
    path('page5/<int:pageID>', views.page5, name='page5'),
    path('create', views.create, name='create'),
    path('cocktailList/<int:pageID>/', views.cocktailList, name='cocktailList'),

]
