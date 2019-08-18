from django.urls import path
from .views import (
    JobListingView, JobListingPagedListView,
    JobListingCreateView, JobListingEditView,
    JobListingDeleteView, JobListingPublishView,
    JobListingCloseView
)


urlpatterns = [
    path('paged', JobListingPagedListView.as_view(), name="job-listings-paged"),
    path('listing/<int:id>', JobListingView.as_view(), name="job-listing"),
    path('new', JobListingCreateView.as_view(), name="job-listing-new"),
    path('edit/<int:id>', JobListingEditView.as_view(), name="job-listing-edit"),
    path('delete/<int:id>', JobListingDeleteView.as_view(), name="job-listing-delete"),
    path('publish/<int:id>', JobListingPublishView.as_view(), name="job-listing-publish"),
    path('close/<int:id>', JobListingCloseView.as_view(), name="job-listing-close")
]
