
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('details', views.user_details, name='details'),
    path('Signup', views.Signup_form, name='Signup'),
    path('edit', views.edit_profile, name='edit'),
    path('change_password', views.change_password, name='change_password'),

]