from django.urls import path
from .views import (
    JobListingView, JobListingPagedListView
)


urlpatterns = [
    path('paged', JobListingPagedListView.as_view(), name="job-listings-paged"),
    path('listing/<int:id>', JobListingView.as_view(), name="job-listing")
]