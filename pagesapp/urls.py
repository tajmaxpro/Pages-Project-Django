from django.urls import path
from .views import HomePageView, AboutPageView, CreatorPage, TutorPage

urlpatterns = [
    path('tutor/', TutorPage.as_view(), name = 'tutor'),
    path('creator/', CreatorPage.as_view(), name = 'creator'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('', HomePageView.as_view(), name = 'home')
]