from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='aboutme'),
    path('skills/', views.skill_s, name='skills'),
    path('projects/', views.project_s, name='projects'),
    path('chalea/', views.cha_lea, name='chalea'),
    path('future/', views.fut_ure, name='future'),
    path('resume/', views.res_ume, name='resume'),
    path('contact/', views.con_tact, name='contact'),
]
