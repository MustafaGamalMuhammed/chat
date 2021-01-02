from django.urls import path
from . import views


auth_urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
]

urlpatterns = []
urlpatterns.extend(auth_urlpatterns)
