from rest_framework.response import Response
from rest_framework.views import APIView
from .models import JobListing
from .services import JobListingService
from .serializers import (
    JobListingSerializer, JobListingSearchFilterSerializer, 
    JobListingSearchResponseSerializer
)


class JobListingPagedListView(APIView):
    def post(self, request):
        search_filter = JobListingSearchFilterSerializer(request.data)
        search_response = JobListingService.get_paged_job_listings(search_filter)
        serialized = JobListingSearchResponseSerializer(search_response)
        return Response(serialized.data)
    

class JobListingView(APIView):
    def get(self, request, id):
        job_listing = JobListingService.get_job_listing_by_id(id)
        serialized = JobListingSerializer(job_listing)
        return Response(serialized.data)
            