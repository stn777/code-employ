from django.urls import path
from .views import JobListingListView, JobListingView


urlpatterns = [
    path('/', JobListingListView.as_view(), name="job-listings-all"),
    path('/<int:id>', JobListingView.as_view(), name="job-listing")
]