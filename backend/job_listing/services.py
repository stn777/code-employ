from .models import JobListing
from django.http import Http404

class JobListingService():

    @staticmethod
    def get_job_listings():
        return JobListing.objects.all()
    
    @staticmethod
    def get_job_listing_by_id(id):
        try:
            return JobListing.objects.get(id=id)
        except JobListing.DoesNotExist:
            raise Http404

        