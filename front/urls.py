
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('index1/', views.index1, name='index1'),	
    path('', views.index, name='index'),	
    path('reading_materials/', views.reading_material, name='reading_material'),	
    path('quizlist/<str:pk>',views.quizlist, name='quizlist'),
     path('quizview/<str:pk>/data',views.quiz_data_view, name='quiz_data_view'),
     
     path('quizview/<str:pk>/save',views.save_quiz_view, name='save_quiz_view'),
     path('quizview/<str:pk>', views.quizview, name='quizview'),
 path('mock_test/', views.mocktest, name='mock_test'),
    path('progress/', views.progress, name='progress'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
     path('contact/', views.send_email_contact, name='contact'),
      path('services/', views.services, name='services'),
path('about/', views.about, name='about'),
path('progress_chart/', views.progress_chart, name='progress_chart'),
#  path('getapi/', getapi, name='getapi'),


    path( 'reset_password/', auth_views.PasswordResetView.as_view(), name = 'reset_password'),
    path( 'PasswordResetDoneView/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name = 'password_reset_done'),
    path( 'reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_form.html'), name = 'password_reset_confirm'),
    path( 'reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_done.html'), name = 'password_reset_complete'),
    ]