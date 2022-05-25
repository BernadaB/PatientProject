from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='home'),
    path('patient/create/', views.PatientCreateView.as_view(), name='patient-create'),
    path('patient/detail/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),
    path('patient/add-to-my-patients/<int:pk>', views.AddToMyPatientsView.as_view(), name='add-to-my-patients'),
    path('search-results', views.SearchResultsView.as_view(), name='search-results')
]
