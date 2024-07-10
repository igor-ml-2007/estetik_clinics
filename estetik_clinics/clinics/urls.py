from django.urls import path
from clinics.views import *


urlpatterns = [
    path('actions/', ActionListAPIView.as_view(), name='actions'),
    path('online-appointments/', OnlineAppointmentCreateAPIView.as_view(), name='online-appointments'),
    path('news-categories/', NewsCategoryListAPIView.as_view(), name='news-categories'),
    path('news/<int:pk>/', NewsDetailAPiView.as_view(), name='news-detail'),
    path('specialists/', SpecialistListAPIView.as_view(), name='specialist-list'),
    path('contact-chief-doctor/', ContactChiefDoctorCreateAPIView.as_view(), name='contact-chief-doctor'),
    path('feedback-list/', FeedbackListAPIView.as_view(), name='feedback_list'),
    path('feedback-create/', FeedbackCreateAPIView.as_view(), name='feedback_create'),
    path('about-us/', AboutUsAPIView.as_view(), name='about_us'),
    path('photogallery-categories/', PhotoGalleryCategoryListAPIView.as_view(), name='photogallery-categories'),
    path('photogalleries/', PhotoGalleryListAPIView.as_view(), name='photogalleries'),
    path('licences/', LicenseListAPIView.as_view(), name='licences'),
    path('specialist/<int:pk>/', SpecialistDetailAPIView.as_view(), name='specialist-detail'),
    path('vacancies/', VacancyListAPIView.as_view(), name='vacancies'),
    path('story-categories/', StoryCategoriesListAPIView.as_view(), name='story-categories'),
    path('home-slider/', HomeSliderListAPIView.as_view(), name='home-slider'),
    path('contacts/', ContactAPIView.as_view(), name='contacts')
]
