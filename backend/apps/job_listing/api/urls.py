from django.urls import path
from .views import (
    JobListingView, JobListingPagedListView,
    JobListingNewView, JobListingEditView
)


urlpatterns = [
    path('paged', JobListingPagedListView.as_view(), name="job-listings-paged"),
    path('listing/<int:id>', JobListingView.as_view(), name="job-listing"),
    path('new', JobListingNewView.as_view(), name="job-listing-new"),
    path('edit/<int:id>', JobListingEditView.as_view(), name="job-listing-edit")
]
