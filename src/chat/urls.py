from django.urls import path
from . import views


index_urlpatterns = [
    path('', views.index, name="index"),
]

auth_urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
]

search_urlpatterns = [
    path('search/<str:q>/', views.search, name="search"),
]

urlpatterns = []
urlpatterns.extend(auth_urlpatterns)
urlpatterns.extend(search_urlpatterns)
urlpatterns.extend(index_urlpatterns)
