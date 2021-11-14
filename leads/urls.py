from django.urls import path
from .views import *

app_name = "leads"
urlpatterns = [
    path('', LeadListView.as_view(), name="lead_list"),
    path('details/<int:pk>', LeadDetailView.as_view(), name="details"),
    path('create', LeadCreateView.as_view(), name="create"),
    path('update/<int:pk>', LeadUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', LeadDeleteView.as_view(), name="delete"),

]