from django.urls import path
from .views import JobListingListView, JobListingView


urlpatterns = [
    path('all', JobListingListView.as_view(), name="job-listings-all"),
    path('listing/<int:id>', JobListingView.as_view(), name="job-listing")
]