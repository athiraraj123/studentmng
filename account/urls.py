from django.urls import path
from . import views

urlpatterns = [
      path('',views.mainhome,name='mainhome'),
      path('contact',views.contact,name='contact'),
      path('course',views.course,name='course'),
      path('gallery',views.gallery,name='gallery'),
      path('signin',views.signin,name='signin'),
      path('signup',views.signup,name='signup'),
      # path('forgot',views.forgot,name='forgot'),
]

