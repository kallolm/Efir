
from django.urls import path
from . import views
from .views import SignUpView


urlpatterns = [
    path("",views.login_request),
    path('signup/', SignUpView.as_view(), name='SignUpView'),
    path('myapp', views.home, name= 'home'),
    path('logout/',views.logout_method,name="logout"),
    path('upload',views.upload,name="upload")
]
