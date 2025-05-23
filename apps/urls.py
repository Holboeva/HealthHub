from django.urls import path
from django.views.generic import TemplateView

from apps.views import \
    nutrition_view, home_page_view, courses_view, recipies_view, blog_view, about_view, aloqa_view, \
    fitness_view, psychology_view, massaj_view, seminar_view, LoginFormView, RegisterCreateView, SendMailFormView

urlpatterns = [
    path('', home_page_view, name='home'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('courses/', courses_view, name='courses'),
    path('recipies/', recipies_view, name='recipies'),
    path('blog/', blog_view, name='blog'),
    path('about/', about_view, name='about'),
    path('aloqa/', aloqa_view, name='aloqa'),
    path('nutrition/', nutrition_view, name='nutrition'),
    path('fitnes/', fitness_view, name='fitness'),
    path('psixologiya/', psychology_view, name='psixologiya'),
    path('massaj/', massaj_view, name='massaj'),
    path('seminar/', seminar_view, name='seminar'),
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('send-email', SendMailFormView.as_view(), name='send_email'),
    path('check-email', RegisterCreateView.as_view(), name='check_email'),

]
