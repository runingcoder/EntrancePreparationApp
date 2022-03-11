
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
    path('ioe_quizlist/<str:pk>',views.ioe_quizlist, name='ioe_quizlist'),
    path('iom_quizlist/<str:pk>',views.iom_quizlist, name='iom_quizlist'),
     path('random_quizlist/<str:pk>',views.random_quizlist, name='random_quizlist'),
     path('quizview/<str:pk>/data',views.quiz_data_view, name='quiz_data_view'),
     
     path('quizview/<str:pk>/save',views.save_quiz_view, name='save_quiz_view'),
     path('quizview/<str:pk>', views.quizview, name='quizview'),
 path('mock_test/', views.mocktest, name='mock_test'),  
 path('ioe_page/<str:pk>/', views.ioe_page, name='ioe_page'),
 path('iom_page/<str:pk>/', views.iom_page, name='iom_page'),
 path('random_page/<str:pk>/', views.random_page, name='random_page'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
     path('contact/', views.send_email_contact, name='contact'),
      path('services/', views.services, name='services'),
path('about/', views.about, name='about'),
path('api/progress/', ChartData.as_view(), name='progress_api'),
#  path('getapi/', getapi, name='getapi'),
path('progress_chart/', views.progressChart, name='progress_chart'),


    path( 'reset_password/', auth_views.PasswordResetView.as_view(), name = 'reset_password'),
    path( 'PasswordResetDoneView/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name = 'password_reset_done'),
    path( 'reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_form.html'), name = 'password_reset_confirm'),
    path( 'reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_done.html'), name = 'password_reset_complete'),
    ]